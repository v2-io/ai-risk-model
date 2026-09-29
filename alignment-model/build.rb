#!/usr/bin/env ruby
# frozen_string_literal: true

# Build the "Aligned to whom?" map from a small markdown file.
#
#   rake                                  # alignment.md -> alignment.html (same as below)
#   ruby build.rb                         # alignment.md -> alignment.html (self-contained)
#   ruby build.rb other.md -o other.html
#   ruby build.rb --link                  # write styles.css and link it + lines.js instead of inlining
#   ruby build.rb --palette               # also write palette.html (every colour class)
#
# Structure lives in templates/*.slim, layout in styles/style.sass and all colour in
# styles/palette.sass; the connector lines are drawn in the browser by lines.js from the
# rendered boxes, so rows and boxes can change size freely and the lines follow.
#
# Markdown format (see alignment.md):
#   optional front matter   key: value lines between --- fences
#   # Title
#   paragraphs              intro; a paragraph starting with ">" becomes the lead
#   ## Stack                table: id | layer | gloss | class | group | parent | size
#   ## Actors               table: display columns... | edges | class
#   ## Notes                paragraphs shown under the table (optional)
#   ## Footnote             paragraphs shown under the stack (optional)

require "bundler/setup"
require "optparse"
require "slim"
require "sass-embedded"

Encoding.default_external = Encoding::UTF_8   # sources are UTF-8 whatever the locale says

module Alignment
  HERE = __dir__
  STYLES = %w[styles/palette.sass styles/style.sass].freeze

  # ------------------------------------------------------------------ markdown bits
  module Markdown
    module_function

    def escape(text)
      text.to_s.gsub("&", "&amp;").gsub("<", "&lt;").gsub(">", "&gt;")
    end

    # Escape HTML, then apply a small subset of inline markdown.
    def inline(text)
      t = escape(text.to_s.strip)
      t = t.gsub(/\\([\\*_`|>#-])/) { "\u0000#{Regexp.last_match(1).ord}\u0000" }
      t = t.gsub(/`([^`]+)`/, '<code>\1</code>')
      t = t.gsub(/\*\*(.+?)\*\*/, '<strong>\1</strong>')
      t = t.gsub(/(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])/, '<em>\1</em>')
      t = t.gsub(/(?<![\w_])_(?!\s)(.+?)(?<!\s)_(?![\w_])/, '<em>\1</em>')
      t = t.gsub(/\[([^\]]+)\]\(([^)\s]+)\)/, '<a href="\2">\1</a>')
      t.gsub(/\u0000(\d+)\u0000/) { Regexp.last_match(1).to_i.chr }
    end

    def split_row(line)
      s = line.strip
      s = s[1..] if s.start_with?("|")
      s = s[0...-1] if s.end_with?("|") && !s.end_with?("\\|")
      s.split(/(?<!\\)\|/, -1).map { |c| c.gsub("\\|", "|").strip }
    end

    # [header, rows] of the first table in `lines` (rows padded to the header's width)
    def table(lines)
      rows = lines.select { |l| l.strip.start_with?("|") }
      return [[], []] if rows.size < 2

      header = split_row(rows[0])
      body = rows[2..].map { |r| split_row(r).then { |c| c + [""] * [header.size - c.size, 0].max } }
      [header, body]
    end

    def paragraphs(lines)
      out = []
      cur = []
      (lines + [""]).each do |l|
        if l.strip.empty? || l.strip.start_with?("|")
          out << cur.map(&:strip).join(" ") unless cur.empty?
          cur = []
        else
          cur << l
        end
      end
      out
    end

    # [meta, title, sections] — sections maps lower-cased "## heading" to its lines;
    # "_intro" holds everything between the title and the first section.
    def parse(md)
      lines = md.gsub(/<!--.*?-->/m, "").lines.map(&:chomp)
      meta = {}
      if lines.first&.strip == "---"
        stop = lines[1..].index("---") + 1
        lines[1...stop].each do |l|
          k, v = l.split(":", 2)
          meta[k.strip] = v.strip if v
        end
        lines = lines[(stop + 1)..]
      end
      title = ""
      sections = { "_intro" => [] }
      name = "_intro"
      lines.each do |l|
        if l.start_with?("# ") && title.empty?
          title = l[2..].strip
        elsif l.start_with?("## ")
          name = l[3..].strip.downcase
          sections[name] = []
        else
          sections[name] << l
        end
      end
      [meta, title, sections]
    end
  end

  # ------------------------------------------------------------------ the model

  Box = Struct.new(:id, :name, :gloss, :classes, :group, :parent, :size, :children, keyword_init: true)
  Group = Struct.new(:name, :classes, :size, :members, keyword_init: true)
  Actor = Struct.new(:cells, :edges, :classes, keyword_init: true)
  Para = Struct.new(:text, :lead, keyword_init: true)

  class Page
    attr_reader :meta, :title, :intro, :headers, :stack, :actors, :referents, :notes, :footnotes

    def initialize(markdown)
      @meta, @title, sec = Markdown.parse(markdown)
      @intro = Markdown.paragraphs(sec["_intro"]).map do |p|
        p.start_with?(">") ? Para.new(text: p.sub(/\A>\s*/, ""), lead: true) : Para.new(text: p, lead: false)
      end
      @stack, ids = parse_stack(sec.fetch("stack", []))
      @headers, @actors, @referents = parse_actors(sec.fetch("actors", []), ids)
      @notes = Markdown.paragraphs(sec.fetch("notes", []))
      @footnotes = Markdown.paragraphs(sec.fetch("footnote", []))
    end

    private

    def parse_stack(lines)
      header, rows = Markdown.table(lines)
      col = header.each_with_index.to_h { |h, i| [h.downcase, i] }
      get = ->(r, k) { col.key?(k) ? r[col[k]] : "" }
      boxes = rows.map do |r|
        Box.new(id: get[r, "id"], name: get[r, "layer"], gloss: get[r, "gloss"], classes: get[r, "class"],
                group: get[r, "group"], parent: get[r, "parent"], size: get[r, "size"], children: [])
      end
      by_id = boxes.to_h { |b| [b.id, b] }
      boxes.each do |b|
        next if b.parent.empty?

        abort "stack: unknown parent #{b.parent.inspect} for #{b.id.inspect}" unless by_id.key?(b.parent)
        by_id[b.parent].children << b
      end
      # top level: consecutive boxes with the same group share one frame
      items = boxes.select { |b| b.parent.empty? }.chunk_while { |a, b| !a.group.empty? && a.group == b.group }.map do |run|
        next run.first if run.first.group.empty?

        Group.new(name: run.first.group, classes: run.first.classes, members: run,
                  size: run.sum { |b| b.size.empty? ? 1.0 : b.size.to_f })
      end
      [items, by_id.keys]
    end

    def parse_actors(lines, stack_ids)
      header, rows = Markdown.table(lines)
      lower = header.map(&:downcase)
      ei = lower.index("edges")
      ci = lower.index("class")
      shown = header.each_index.reject { |i| [ei, ci].include?(i) }
      actors = rows.map do |r|
        edges = (ei ? r[ei].split(",").map(&:strip).reject(&:empty?) : []).map do |e|
          id, weight = e.split(":", 2).map(&:strip)
          unless stack_ids.include?(id)
            abort "actor #{r[0].inspect}: unknown edge target #{id.inspect} (stack ids: #{stack_ids.sort.join(', ')})"
          end
          "#{id}:#{weight.to_s.empty? ? '1' : weight}"
        end
        Actor.new(cells: shown.map { |i| r[i] }, edges: edges, classes: ci ? r[ci].strip : "")
      end
      referent = ->(a) { a.classes.split.include?("referent") }
      [shown.map { |i| header[i] }, actors.reject(&referent), actors.select(&referent)]
    end
  end

  # ------------------------------------------------------------------ rendering

  # The scope templates render in: helpers plus the page.
  class View
    attr_reader :page

    def initialize(page = nil, link: false)
      @page = page
      @link = link
    end

    def md(text) = Markdown.inline(text)

    def template(name) = (@templates ||= {})[name] ||= Slim::Template.new(File.join(HERE, "templates", "#{name}.slim"))

    def partial(name, **locals) = template(name).render(self, locals)

    def css = STYLES.map { |f| Sass.compile(File.join(HERE, f)).css }.join("\n\n")

    def styles
      return %(<link rel="stylesheet" href="styles.css">) if @link

      "<style>\n#{css}\n</style>"
    end

    def script
      return %(<script src="lines.js"></script>) if @link

      "<script>\n#{File.read(File.join(HERE, 'lines.js'))}\n</script>"
    end

    def families = File.read(File.join(HERE, "styles/palette.sass"))[/^\$families:(.*)$/, 1].split("//").first.scan(/"([a-z]+)"/).flatten

    def number(x) = format("%g", x)
  end

  module_function

  def build(md_path, out_path, link: false)
    view = View.new(Page.new(File.read(md_path)), link: link)
    File.write(File.join(File.dirname(out_path), "styles.css"), view.css) if link
    File.write(out_path, view.partial("page"))
    puts "wrote #{out_path}"
  end

  def build_palette(out_path)
    File.write(out_path, View.new.partial("palette"))
    puts "wrote #{out_path}"
  end
end

if $PROGRAM_NAME == __FILE__
  opts = { link: false, palette: false, out: nil }
  OptionParser.new do |o|
    o.banner = "usage: ruby build.rb [markdown] [-o out.html] [--link] [--palette]"
    o.on("-o", "--out FILE", "output file (default: the markdown's name with .html)") { |v| opts[:out] = v }
    o.on("--link", "write styles.css and link it + lines.js instead of inlining them") { opts[:link] = true }
    o.on("--palette", "also write palette.html showing every colour class") { opts[:palette] = true }
  end.parse!
  md = ARGV.first || File.join(Alignment::HERE, "alignment.md")
  Alignment.build_palette(File.join(Alignment::HERE, "palette.html")) if opts[:palette]
  Alignment.build(md, opts[:out] || md.sub(/\.[^.\/]+\z/, "") + ".html", link: opts[:link])
end

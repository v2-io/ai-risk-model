// Lexicon page behaviour: filter the contents, mark what is open, step between groups
// with the arrow keys, and switch light/dark. The page works without any of it
// (views are switched by CSS :target).
(function () {
  var input = document.getElementById("filter");
  var groups = Array.prototype.slice.call(document.querySelectorAll(".toc-group"));
  var items = Array.prototype.slice.call(document.querySelectorAll(".toc-group li"));

  // filter: hide non-matching terms, and a group whose terms are all hidden
  if (input) {
    input.addEventListener("input", function () {
      var q = input.value.trim().toLowerCase();
      items.forEach(function (li) {
        li.classList.toggle("hidden", q !== "" && li.dataset.words.indexOf(q) < 0);
      });
      groups.forEach(function (g) {
        g.classList.toggle("empty", q !== "" && !g.querySelector("li:not(.hidden)"));
      });
    });
    input.addEventListener("keydown", function (e) {
      if (e.key !== "Enter") return;
      var first = items.filter(function (li) { return !li.classList.contains("hidden"); })[0];
      if (first) location.hash = first.querySelector("a").getAttribute("href");
    });
  }

  // mark the open term (or group) in the contents
  function mark() {
    var hash = location.hash;
    document.querySelectorAll(".toc .here").forEach(function (el) { el.classList.remove("here"); });
    if (!hash) return;
    var link = document.querySelector('.toc a[href="' + hash + '"]');
    if (!link) return;
    (link.parentElement.tagName === "LI" ? link.parentElement : link).classList.add("here");
    if (link.scrollIntoViewIfNeeded) link.scrollIntoViewIfNeeded(false);
  }
  window.addEventListener("hashchange", function () {
    // a group opens at its top; a term's card is brought into view by the browser
    var el = location.hash && document.getElementById(location.hash.slice(1));
    if (!el || el.classList.contains("view")) window.scrollTo(0, 0);
    mark();
  });
  mark();

  // ← and → step to the previous and next group from the open view
  document.addEventListener("keydown", function (e) {
    if (e.target.tagName === "INPUT" || e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
    var target = location.hash && document.getElementById(location.hash.slice(1));
    var view = target && (target.closest(".view"));
    var link = view && view.querySelector('.pager a[data-key="' + e.key + '"]');
    if (link) { e.preventDefault(); location.hash = link.getAttribute("href"); }
  });

  // theme: the OS setting until the button is used; the choice is remembered if storage allows
  var root = document.documentElement;
  try { var saved = localStorage.getItem("lexicon-theme"); if (saved) root.dataset.theme = saved; } catch (e) {}
  var button = document.getElementById("theme");
  if (button) {
    button.addEventListener("click", function () {
      var dark = root.dataset.theme
        ? root.dataset.theme === "dark"
        : window.matchMedia("(prefers-color-scheme: dark)").matches;
      root.dataset.theme = dark ? "light" : "dark";
      try { localStorage.setItem("lexicon-theme", root.dataset.theme); } catch (e) {}
    });
  }
})();

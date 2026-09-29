/* Draws the connector lines from actor rows to stack layers.
   Reads the rendered layout, so CSS changes never need coordinate edits.

   Each row carries data-edges="layerId:weight ...".  Each .layer carries
   data-layer="id" and a CSS custom property --edge (the line colour).
   Endpoints are spread evenly down the target box; for a box that contains
   other boxes (e.g. context around the goals) they go in its largest open
   gap. Tweak the look with the CONFIG below. */
(function () {
  const CONFIG = {
    width:   w => 0.35 + 0.95 * w,           // stroke width by weight
    opacity: w => Math.min(1, 0.4 + 0.25 * w),
    radius:  w => 2.2 + 0.4 * w,             // end-dot radius
    inset:   0.12,                            // keep endpoints off box edges (fraction)
    bend:    0.5,                             // control-point position across the gutter
  };
  const NS = 'http://www.w3.org/2000/svg';

  function openInterval(box, top) {
    // [a, b] in svg coordinates: the box, minus its own heading and nested boxes
    const r = box.getBoundingClientRect();
    const kids = [...box.children].filter(k => k.classList.contains('layer'));
    if (!kids.length) return [r.top - top, r.bottom - top];
    const head = box.querySelector(':scope > .layer-head').getBoundingClientRect();
    let cuts = [[r.top, head.bottom], ...kids.map(k => { const q = k.getBoundingClientRect(); return [q.top, q.bottom]; }), [r.bottom, r.bottom]];
    cuts.sort((p, q) => p[0] - q[0]);
    let best = [r.top, r.bottom], size = -1, at = r.top;
    for (const [a, b] of cuts) {
      if (a - at > size) { size = a - at; best = [at, a]; }
      at = Math.max(at, b);
    }
    return [best[0] - top, best[1] - top];
  }

  function draw() {
    const map = document.querySelector('.map');
    const svg = map && map.querySelector('svg.edges');
    if (!svg) return;
    svg.replaceChildren();
    const s = svg.getBoundingClientRect();
    svg.setAttribute('viewBox', `0 0 ${s.width} ${s.height}`);

    // collect edges per target, in row order
    const incoming = new Map();
    map.querySelectorAll('.actors .row[data-edges]').forEach((row, i) => {
      const r = row.getBoundingClientRect();
      for (const e of row.dataset.edges.split(/\s+/).filter(Boolean)) {
        const [id, w] = e.split(':');
        if (!incoming.has(id)) incoming.set(id, []);
        incoming.get(id).push({ y: (r.top + r.bottom) / 2 - s.top, w: parseFloat(w) || 1 });
      }
    });

    for (const [id, list] of incoming) {
      const box = map.querySelector(`.layer[data-layer="${CSS.escape(id)}"]`);
      if (!box) { console.warn('no stack layer', id); continue; }
      const [a0, b0] = openInterval(box, s.top);
      const pad = (b0 - a0) * CONFIG.inset, a = a0 + pad, b = b0 - pad;
      const x2 = box.getBoundingClientRect().left - s.left;
      const colour = getComputedStyle(box).getPropertyValue('--edge').trim() || '#888';
      const cx = s.width * CONFIG.bend;
      list.forEach((e, k) => {
        const y2 = list.length === 1 ? (a + b) / 2 : a + (b - a) * k / (list.length - 1);
        const p = document.createElementNS(NS, 'path');
        p.setAttribute('d', `M0,${e.y} C${cx},${e.y} ${cx},${y2} ${x2},${y2}`);
        p.setAttribute('stroke', colour);
        p.setAttribute('stroke-width', CONFIG.width(e.w));
        p.setAttribute('stroke-opacity', CONFIG.opacity(e.w));
        const c = document.createElementNS(NS, 'circle');
        c.setAttribute('cx', x2); c.setAttribute('cy', y2);
        c.setAttribute('r', CONFIG.radius(e.w)); c.setAttribute('fill', colour);
        svg.append(p, c);
      });
    }
  }

  const redraw = () => requestAnimationFrame(draw);
  window.addEventListener('load', redraw);
  window.addEventListener('resize', redraw);
  if (document.fonts) document.fonts.ready.then(redraw);
  if (window.ResizeObserver) new ResizeObserver(redraw).observe(document.body);
  redraw();
})();

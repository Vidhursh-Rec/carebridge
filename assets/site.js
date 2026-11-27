// Carepedia interactions: window back/forward, mobile menu, random article,
// sidebar search, contents toggle, pipeline steps, language demo.
(function () {
  var PAGES = [
    ["carebridge.html", "CareBridge"], ["how-it-works.html", "How it works"], ["features.html", "Features"],
    ["languages.html", "Languages"], ["design.html", "Design"], ["origin.html", "Build to Care"],
    ["reliability.html", "Reliability"], ["technology.html", "Technology"], ["roadmap.html", "Roadmap"],
    ["history.html", "Revision history"], ["about.html", "About Carepedia"]
  ];
  var here = location.pathname.split("/").pop() || "index.html";

  function on(sel, ev, fn) {
    document.querySelectorAll(sel).forEach(function (el) { el.addEventListener(ev, fn); });
  }

  // Window chrome
  on("[data-back]", "click", function () { history.back(); });
  on("[data-forward]", "click", function () { history.forward(); });
  var win = document.querySelector(".window");
  on("[data-menu]", "click", function (e) {
    var open = win.classList.toggle("nav-open");
    e.currentTarget.setAttribute("aria-expanded", String(open));
  });
  on(".main", "click", function () {
    if (win.classList.contains("nav-open")) {
      win.classList.remove("nav-open");
      document.querySelector("[data-menu]").setAttribute("aria-expanded", "false");
    }
  });

  // Random article
  on("[data-random]", "click", function (e) {
    e.preventDefault();
    var pool = PAGES.filter(function (p) { return p[0] !== here; });
    location.href = pool[Math.floor(Math.random() * pool.length)][0];
  });

  // Contents [hide]/[show]
  on(".toc-toggle", "click", function (e) {
    var toc = e.currentTarget.closest(".toc");
    var collapsed = toc.classList.toggle("collapsed");
    e.currentTarget.textContent = collapsed ? "show" : "hide";
    e.currentTarget.setAttribute("aria-expanded", String(!collapsed));
  });

  // Search: the sidebar form submits to all-pages.html?q=…  "Go" jumps straight to a single match.
  var list = document.querySelector(".allpages");
  if (list) {
    var params = new URLSearchParams(location.search);
    var q = (params.get("q") || "").trim().toLowerCase();
    var status = document.querySelector(".search-status");
    var input = document.querySelector(".search input");
    if (q) {
      if (input) input.value = params.get("q");
      var hits = [];
      list.querySelectorAll("li").forEach(function (li) {
        var match = li.getAttribute("data-title").indexOf(q) !== -1;
        li.classList.toggle("hit", match);
        li.classList.toggle("miss", !match);
        if (match) hits.push(li.querySelector("a").getAttribute("href"));
      });
      if (params.get("go") && hits.length >= 1) {
        // Prefer a page whose title matches; otherwise the page whose text mentions the word, skipping the Main page.
        var titled = [].filter.call(list.querySelectorAll("li.hit > a"), function (a) { return a.textContent.toLowerCase().indexOf(q) !== -1; });
        var other = hits.filter(function (h) { return h !== "index.html"; });
        location.replace(titled.length ? titled[0].getAttribute("href") : (other[0] || hits[0]));
        return;
      }
      status.textContent = hits.length
        ? hits.length + (hits.length === 1 ? " page matches" : " pages match") + " “" + params.get("q") + "”."
        : "No page matches “" + params.get("q") + "”. Try medicine, family, doctor or Tamil.";
    }
  }

  // How it works: click a step to read it
  var detail = document.querySelector(".pipe-detail");
  function pick(li) {
    document.querySelectorAll(".pipeline li").forEach(function (x) { x.classList.toggle("on", x === li); });
    detail.innerHTML = "<b>" + li.querySelector("b").textContent + "</b> – " + li.querySelector("span").textContent;
  }
  if (detail) {
    var steps = document.querySelectorAll(".pipeline li");
    steps.forEach(function (li) {
      li.addEventListener("click", function () { pick(li); });
      li.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); pick(li); } });
    });
    pick(steps[0]);
  }

  // Languages: one reminder, three languages; the drug name never changes
  on(".lang-pick button", "click", function (e) {
    var lang = e.currentTarget.getAttribute("data-lang");
    document.querySelectorAll(".lang-pick button").forEach(function (b) { b.setAttribute("aria-selected", String(b === e.currentTarget)); });
    var rest = document.querySelector(".reminder .rest");
    rest.textContent = rest.getAttribute("data-" + lang);
    rest.setAttribute("lang", lang);
  });
})();

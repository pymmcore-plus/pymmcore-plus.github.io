// Interactive bits for the unified pymmcore-plus docs.
// Runs on every page load, including zensical's instant navigation (document$).

(() => {
  "use strict";

  const ORIGINS = {
    added: { label: "✨ Added", badge: "pymmcore-plus" },
    overridden: { label: "➕ Overridden", badge: "overridden" },
    inherited: { label: "Inherited", badge: null },
  };

  // -------------------------------------------------------------------------
  // Method explorer: filters for table.pymm-explorer (see pymmcore-plus _gen.py)
  // -------------------------------------------------------------------------

  function initExplorer(table) {
    if (table.dataset.pymmReady) return;
    table.dataset.pymmReady = "1";
    const rows = [...table.tBodies[0].rows];
    const state = { origin: "all", category: "", text: "", deprecated: false };

    const toolbar = document.createElement("div");
    toolbar.className = "pymm-explorer-toolbar";

    const search = Object.assign(document.createElement("input"), {
      type: "search",
      placeholder: "Filter methods (name or description)…",
      ariaLabel: "Filter methods",
    });
    search.addEventListener("input", () => {
      state.text = search.value.trim().toLowerCase();
      apply();
    });
    toolbar.append(search);

    const chips = [];
    const count = (o) => rows.filter((r) => o === "all" || r.dataset.origin === o).length;
    for (const [key, label] of [["all", "All"], ...Object.entries(ORIGINS).map(([k, v]) => [k, v.label])]) {
      const chip = document.createElement("button");
      chip.type = "button";
      chip.className = "pymm-chip";
      chip.dataset.origin = key;
      chip.innerHTML = `${label}<span class="pymm-chip__count">${count(key)}</span>`;
      chip.addEventListener("click", () => {
        state.origin = key;
        apply();
      });
      chips.push(chip);
      toolbar.append(chip);
    }

    const select = document.createElement("select");
    select.ariaLabel = "Category";
    const categories = new Map();
    for (const row of rows) {
      categories.set(row.dataset.category, row.cells[2].textContent.trim());
    }
    select.append(new Option("All categories", ""));
    for (const [value, text] of [...categories].sort((a, b) => a[1].localeCompare(b[1]))) {
      select.append(new Option(text, value));
    }
    select.addEventListener("change", () => {
      state.category = select.value;
      apply();
    });
    toolbar.append(select);

    const deprecated = document.createElement("label");
    deprecated.innerHTML = '<input type="checkbox"> show deprecated';
    deprecated.querySelector("input").addEventListener("change", (e) => {
      state.deprecated = e.target.checked;
      apply();
    });
    toolbar.append(deprecated);

    const status = document.createElement("span");
    status.className = "pymm-explorer-count";
    toolbar.append(status);

    (table.closest(".md-typeset__scrollwrap") || table).before(toolbar);

    function apply() {
      let shown = 0;
      for (const row of rows) {
        const visible =
          (state.origin === "all" || row.dataset.origin === state.origin) &&
          (!state.category || row.dataset.category === state.category) &&
          (state.deprecated || row.dataset.deprecated !== "true") &&
          (!state.text || row.textContent.toLowerCase().includes(state.text));
        row.classList.toggle("pymm-hidden", !visible);
        shown += visible;
      }
      for (const chip of chips) {
        chip.setAttribute("aria-pressed", String(chip.dataset.origin === state.origin));
      }
      status.textContent = `${shown} of ${rows.length}`;
    }
    apply();
    decorateHeadings(table, rows);
  }

  // Add an origin badge to each member heading documented on the page.
  function decorateHeadings(table, rows) {
    const prefix = table.dataset.object;
    for (const row of rows) {
      const origin = ORIGINS[row.dataset.origin];
      if (!origin.badge) continue;
      const name = row.querySelector("code").textContent;
      const heading = document.getElementById(`${prefix}.${name}`);
      if (!heading || heading.querySelector(".pymm-heading-origin")) continue;
      const badge = document.createElement("span");
      badge.className = `pymm-heading-origin pymm-heading-origin--${row.dataset.origin}`;
      badge.textContent = origin.badge;
      badge.title = row.querySelector(".pymm-origin")?.title || "";
      const anchor = heading.querySelector(".headerlink");
      anchor ? anchor.before(badge) : heading.append(badge);
    }
  }

  // -------------------------------------------------------------------------
  // Install builder: rewrites the pip/uv commands in [data-pymm-installer]
  // -------------------------------------------------------------------------

  const INSTALL_OPTIONS = [
    { id: "io", label: "Save to OME-Zarr / OME-TIFF", hint: "pymmcore-plus[io]", group: "core" },
    { id: "widgets", label: "Qt widgets", hint: "pymmcore-widgets", group: "gui" },
    { id: "gui", label: "pymmcore-gui app", hint: "from GitHub", group: "gui" },
    { id: "napari", label: "napari plugin", hint: "napari-micromanager", group: "gui" },
  ];

  // What each package already brings in (from their pyproject dependencies):
  // pymmcore-gui -> pymmcore-plus[cli], pymmcore-widgets, ome-writers (= [io]), PyQt6
  // napari-micromanager -> pymmcore-widgets -> pymmcore-plus[cli]
  function implied(opts) {
    return {
      widgets: opts.gui || opts.napari,
      io: opts.gui,
      qt: opts.gui ? "PyQt6" : null,
    };
  }

  // The fewest packages that install everything selected.
  function packages(opts) {
    const qt = implied(opts).qt || opts.qt;
    const pkgs = [];
    if (opts.gui) pkgs.push("git+https://github.com/pymmcore-plus/pymmcore-gui");
    if (opts.napari) {
      pkgs.push(opts.gui ? "napari-micromanager" : `"napari-micromanager[${qt.toLowerCase()}]"`);
    }
    if (opts.widgets && !opts.gui && !opts.napari) pkgs.push(`"pymmcore-widgets[${qt}]"`);
    if (!pkgs.length) pkgs.push(`"pymmcore-plus[${opts.io ? "cli,io" : "cli"}]"`);
    else if (opts.io && !opts.gui) pkgs.push(`"pymmcore-plus[io]"`);
    return pkgs;
  }

  function initInstaller(root) {
    if (root.dataset.pymmReady) return;
    root.dataset.pymmReady = "1";
    const form = document.createElement("form");
    form.className = "pymm-installer-form";
    form.innerHTML = `
      <fieldset><legend>pymmcore-plus</legend>
        <label><input type="checkbox" checked disabled> core + <code>mmcore</code> CLI</label>
        ${INSTALL_OPTIONS.filter((o) => o.group === "core").map(checkbox).join("")}
      </fieldset>
      <fieldset><legend>User interfaces</legend>
        ${INSTALL_OPTIONS.filter((o) => o.group === "gui").map(checkbox).join("")}
      </fieldset>
      <fieldset><legend>Qt backend</legend>
        <label><input type="radio" name="qt" value="PyQt6" checked> PyQt6</label>
        <label><input type="radio" name="qt" value="PySide6"> PySide6</label>
        <small class="pymm-installer-note"></small>
      </fieldset>`;
    root.prepend(form);

    const input = (name) => form.querySelector(`input[name="${name}"]`);
    const radios = [...form.querySelectorAll('input[name="qt"]')];
    // remember what the user chose, so implied options can be restored
    const chosen = { io: false, widgets: false, gui: false, napari: false, qt: "PyQt6" };

    const [pip, uv] = root.querySelectorAll(".tabbed-block pre code");
    function update(event) {
      const target = event?.target;
      if (target?.name === "qt") chosen.qt = target.value;
      else if (target?.name in chosen) chosen[target.name] = target.checked;

      const imp = implied(chosen);
      for (const name of ["io", "widgets"]) {
        input(name).disabled = Boolean(imp[name]);
        input(name).checked = Boolean(imp[name]) || chosen[name];
        input(name).closest("label").title = imp[name] ? "included with your selection" : "";
      }
      const anyQt = chosen.widgets || chosen.gui || chosen.napari;
      for (const radio of radios) {
        radio.disabled = !anyQt || Boolean(imp.qt);
        radio.checked = radio.value === (imp.qt || chosen.qt);
      }
      form.querySelector(".pymm-installer-note").textContent = imp.qt
        ? "pymmcore-gui uses PyQt6"
        : "";

      const pkgs = packages(chosen).join(" ");
      const adapters = "mmcore install  # Micro-Manager device adapters";
      if (pip) pip.textContent = `pip install ${pkgs}\n${adapters}`;
      if (uv) uv.textContent = `uv add ${pkgs}\nuv run ${adapters}`;
    }
    form.addEventListener("change", update);
    update();
  }

  function checkbox(o) {
    return `<label><input type="checkbox" name="${o.id}"> ${o.label} <small>${o.hint}</small></label>`;
  }

  // -------------------------------------------------------------------------

  function init() {
    document.querySelectorAll("table.pymm-explorer").forEach(initExplorer);
    document.querySelectorAll("[data-pymm-installer]").forEach(initInstaller);
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(init);
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();

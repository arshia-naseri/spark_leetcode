// Spark LeetCode web UI: problem list and a three-panel workspace.
"use strict";

const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => [...document.querySelectorAll(sel)];

function store(key, value) {
  try {
    if (value === undefined) return localStorage.getItem(key);
    localStorage.setItem(key, value);
  } catch { /* Storage is not available. */ }
  return null;
}

function esc(text) {
  return String(text).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
}

async function api(path, options = {}) {
  const res = await fetch(path, {
    ...options,
    headers: { "Content-Type": "application/json" },
    body: options.body && JSON.stringify(options.body),
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.error || res.statusText);
  return data;
}

// Lucide icon as an SVG string. Static icons in index.html use data-lucide.
function icon(name) {
  const [tag, attrs, children] = lucide.icons[name];
  return lucide.createElement([tag, { ...attrs, class: "lucide" }, children]).outerHTML;
}

lucide.createIcons();

// ---------- Routing ----------

function route() {
  const m = location.pathname.match(/^\/p\/(\w+)/);
  $("#list-page").hidden = !!m;
  $("#problem-page").hidden = !m;
  if (m) openProblem(m[1]);
  else showList();
}

function go(path) {
  flushSave();
  history.pushState(null, "", path);
  route();
}

document.addEventListener("click", (e) => {
  const a = e.target.closest("a[href^='/']");
  if (!a || e.metaKey || e.ctrlKey || e.shiftKey) return;
  e.preventDefault();
  go(a.getAttribute("href"));
});
window.addEventListener("popstate", () => { flushSave(); route(); });

// ---------- List page ----------

let problems = [];
let diffFilter = "";

async function showList() {
  document.title = "Spark LeetCode";
  problems = await api("/api/problems");
  renderList();
  $("#search").focus();
}

function renderList() {
  const q = $("#search").value.trim().toLowerCase();
  const rows = problems.filter((p) =>
    (!diffFilter || p.difficulty === diffFilter) &&
    (!q || p.title.toLowerCase().includes(q) || String(p.number).startsWith(q)));
  $("#count").textContent = `${rows.length} / ${problems.length}`;
  $("#problem-list").innerHTML = rows.length ? rows.map((p) => `
    <a class="problem-row" href="/p/${p.name}">
      ${statusIcon(p)}
      <span class="problem-title">${esc(p.title)}</span>
      <span class="diff-${p.difficulty}">${cap(p.difficulty)}</span>
    </a>`).join("") : `<div class="empty">No questions found.</div>`;
}

function statusIcon(p) {
  if (p.solved.length) {
    const how = p.solved.map((m) => (m === "sql" ? "SQL" : "DataFrame")).join(" and ");
    return `<span class="dot-solved" title="Solved: ${how}">${icon("Check")}</span>`;
  }
  if (p.attempted) return `<span class="dot-attempted" title="Attempted: a practice file has changes">${icon("CircleDot")}</span>`;
  return "<span></span>";
}

const cap = (s) => s[0].toUpperCase() + s.slice(1);

$("#search").addEventListener("input", renderList);
$("#diff-filter").addEventListener("click", (e) => {
  const btn = e.target.closest("button");
  if (!btn) return;
  diffFilter = btn.dataset.diff;
  $$("#diff-filter .chip").forEach((b) => b.classList.toggle("active", b === btn));
  renderList();
});

// ---------- Problem page ----------

let current = null; // The loaded problem.
let editor = null;
let solutionView = null;
let method = store("method") || "dataframe";
let saveTimer = null;
let lastResult = null;

function initEditor() {
  editor = CodeMirror($("#editor"), {
    mode: "python",
    theme: "material-darker",
    lineNumbers: true,
    indentUnit: 4,
    tabSize: 4,
    matchBrackets: true,
    autoCloseBrackets: true,
    extraKeys: {
      Tab: (cm) => cm.somethingSelected() ? cm.indentSelection("add") : cm.replaceSelection("    "),
      "Shift-Tab": (cm) => cm.indentSelection("subtract"),
      "Cmd-/": "toggleComment",
      "Ctrl-/": "toggleComment",
      "Cmd-Enter": run,
      "Ctrl-Enter": run,
      "Cmd-S": flushSave,
      "Ctrl-S": flushSave,
      "Ctrl-Space": showHints,
    },
  });
  // Show completions while the user types a name, after a ".", or in call arguments after "(" or ",".
  editor.on("inputRead", (cm, change) => {
    if (cm.state.completionActive || change.text.length !== 1) return;
    const cur = cm.getCursor();
    const before = cm.getLine(cur.line).slice(0, cur.ch);
    const inArgs = /[(,]\s*$/.test(before);
    if (!inArgs && !/[A-Za-z_.]$/.test(before)) return;
    const type = cm.getTokenAt(cur).type || "";
    if (!/string|comment/.test(type)) showHints(cm, inArgs);
  });
  editor.on("change", (_cm, change) => {
    if (change.origin === "setValue") return;
    if (current) current.code[method] = editor.getValue();
    $("#save-state").textContent = "Saving…";
    clearTimeout(saveTimer);
    saveTimer = setTimeout(save, 800);
  });
  editor.on("cursorActivity", (cm) => {
    const c = cm.getCursor();
    $("#cursor").textContent = `Ln ${c.line + 1}, Col ${c.ch + 1}`;
    updateSignature(cm);
  });
  editor.on("blur", hideSignature);
  editor.on("keydown", (_cm, e) => { if (e.key === "Escape") hideSignature(); });
}

// ---------- Completions (jedi on the server) ----------

const KIND_LETTER = { function: "ƒ", class: "C", module: "M", instance: "v", param: "p", statement: "v", keyword: "k", property: "p", path: "/" };

// paramsOnly: after "(" or ",", show the list only when the call has keyword arguments (not for "," in a list).
function showHints(cm, paramsOnly = false) {
  const hint = (cm2, callback) => pythonHint(cm2, callback, paramsOnly);
  hint.async = true;
  cm.showHint({ hint, completeSingle: false });
}

function pythonHint(cm, callback, paramsOnly = false) {
  if (!current) return callback(null);
  const cur = cm.getCursor();
  const code = cm.getValue();
  api(`/api/problems/${current.name}/complete`, { method: "POST", body: { code, method, line: cur.line + 1, ch: cur.ch } })
    .then(({ from_ch, items }) => {
      if (!items.length) return callback(null);
      if (paramsOnly && from_ch === cur.ch && !items.some((it) => it.name.endsWith("="))) return callback(null);
      const data = {
        list: items.map((it) => ({ text: it.name, kind: it.type, render: renderHint })),
        from: CodeMirror.Pos(cur.line, from_ch),
        to: CodeMirror.Pos(cur.line, cur.ch),
      };
      CodeMirror.on(data, "select", (item, el) => showDoc(item, el, code, cur));
      CodeMirror.on(data, "close", hideDoc);
      callback(data);
    })
    .catch(() => callback(null));
}

function renderHint(el, _data, item) {
  el.innerHTML = `<span class="hint-kind kind-${esc(item.kind)}">${KIND_LETTER[item.kind] || "·"}</span>${esc(item.text)}`;
}

// The signature and docstring of the selected completion, next to the list.
let docTimer = null;
const docCache = new Map();

function hideDoc() {
  clearTimeout(docTimer);
  const box = $("#hint-doc");
  if (box) box.remove();
}

function showDoc(item, el, code, cur) {
  clearTimeout(docTimer);
  docTimer = setTimeout(async () => {
    const key = `${cur.line}:${cur.ch}:${code.length}:${item.text}`;
    if (!docCache.has(key)) {
      if (docCache.size > 200) docCache.clear();
      docCache.set(key, api(`/api/problems/${current.name}/describe`, {
        method: "POST", body: { code, method, line: cur.line + 1, ch: cur.ch, name: item.text },
      }).catch(() => null));
    }
    const info = await docCache.get(key);
    const list = el.parentNode;
    if (!info || (!info.signature && !info.doc) || !list.isConnected || !el.classList.contains("CodeMirror-hint-active")) return hideDoc();
    let box = $("#hint-doc");
    if (!box) {
      box = document.createElement("div");
      box.id = "hint-doc";
      document.body.appendChild(box);
    }
    box.innerHTML = (info.signature ? `<div class="hint-sig">${esc(info.signature)}</div>` : "")
      + (info.doc ? `<div class="hint-body">${esc(info.doc)}</div>` : "");
    const rect = list.getBoundingClientRect();
    const right = rect.right + 4 + 420 <= window.innerWidth;
    box.style.top = `${rect.top}px`;
    box.style.left = right ? `${rect.right + 4}px` : "";
    box.style.right = right ? "" : `${window.innerWidth - rect.left + 4}px`;
  }, 120);
}

// ---------- Signature help: the call that has the cursor in its arguments ----------

let sigTimer = null;
let sigSeq = 0;

function hideSignature() {
  clearTimeout(sigTimer);
  sigSeq++;
  const box = $("#sig-help");
  if (box) box.remove();
}

function updateSignature(cm) {
  clearTimeout(sigTimer);
  if (!current || cm.somethingSelected()) return hideSignature();
  const seq = ++sigSeq;
  sigTimer = setTimeout(async () => {
    const cur = cm.getCursor();
    const info = await api(`/api/problems/${current.name}/signature`, {
      method: "POST", body: { code: cm.getValue(), method, line: cur.line + 1, ch: cur.ch },
    }).catch(() => null);
    if (seq !== sigSeq) return; // The cursor moved again.
    if (!info || !info.name) return hideSignature();
    let box = $("#sig-help");
    if (!box) {
      box = document.createElement("div");
      box.id = "sig-help";
      document.body.appendChild(box);
    }
    const params = info.params.map((p, i) => i === info.index ? `<b class="sig-active">${esc(p)}</b>` : esc(p));
    box.innerHTML = `<div class="hint-sig">${esc(info.name)}(${params.join(", ")})${esc(info.returns)}</div>`
      + (info.param_doc ? `<div class="sig-param">${esc(info.param_doc)}</div>` : "")
      + (info.doc ? `<div class="hint-body">${esc(info.doc)}</div>` : "");
    // Put the box above the cursor line (the completion list opens below it). Below if no space.
    const at = cm.cursorCoords(cur, "window");
    const above = at.top - box.offsetHeight - 4;
    box.style.left = `${Math.max(4, Math.min(at.left, window.innerWidth - box.offsetWidth - 4))}px`;
    box.style.top = `${above >= 4 ? above : at.bottom + 4}px`;
  }, 150);
}

async function save() {
  clearTimeout(saveTimer);
  saveTimer = null;
  if (!current) return;
  await api(`/api/problems/${current.name}/code`, { method: "PUT", body: { code: editor.getValue(), method } });
  $("#save-state").textContent = "Saved";
}

function flushSave() {
  if (saveTimer) save();
}

async function openProblem(name) {
  if (!editor) initEditor();
  if (current && current.name === name) return;
  current = null;
  lastResult = null;
  $("#description").innerHTML = `<p class="placeholder"><span class="spinner"></span>Loading…</p>`;
  let p;
  try {
    p = await api(`/api/problems/${name}`);
  } catch (err) {
    $("#description").innerHTML = `<div class="error-box">${esc(err.message)}</div>`;
    return;
  }
  current = p;
  document.title = p.title;

  // Description: drop the "Run" section with the shell commands.
  const md = p.question.replace(/\n## Run\n[\s\S]*$/, "");
  $("#description").innerHTML = `<div class="md">${marked.parse(md)}</div>`;
  const diffLine = [...$$("#description p")].find((el) => el.textContent.startsWith("Difficulty:"));
  if (diffLine) {
    const link = diffLine.querySelector("a");
    diffLine.innerHTML = `<span class="badge diff-${p.difficulty}">${cap(p.difficulty)}</span>`
      + (link ? ` &nbsp;<a href="${esc(link.href)}" target="_blank" rel="noopener">LeetCode ${icon("ExternalLink")}</a>` : "");
  }
  $$("#description a[href^='http']").forEach((a) => { a.target = "_blank"; a.rel = "noopener"; });

  // Solution: hidden until the user asks for it.
  $("#solution-cover").hidden = false;
  $("#solution-code").hidden = true;
  $("#solution-code").innerHTML = "";
  solutionView = null;
  selectTab("left", "description");

  showCode();

  renderTestcases(0);
  $("#result").innerHTML = `<p class="placeholder">Press <b>Run</b> (Ctrl/⌘ + Enter) to test your code.</p>`;
  selectTab("test-panel", "testcase");
}

function selectTab(panelId, tab) {
  $$(`#${panelId} .tab[data-tab]`).forEach((b) => b.classList.toggle("active", b.dataset.tab === tab));
  $$(`#${panelId} .tab[data-tab]`).forEach((b) => { $(`#${b.dataset.tab}`).hidden = b.dataset.tab !== tab; });
}

$$(".tabs").forEach((bar) => bar.addEventListener("click", (e) => {
  const btn = e.target.closest(".tab[data-tab]");
  if (btn) selectTab(bar.closest(".panel").id, btn.dataset.tab);
}));

$("#reveal").addEventListener("click", () => {
  $("#solution-cover").hidden = true;
  $("#solution-code").hidden = false;
  if (!solutionView) {
    solutionView = CodeMirror($("#solution-code"), {
      value: current.solution, mode: "python", theme: "material-darker",
      readOnly: true, lineNumbers: true, lineWrapping: true, viewportMargin: Infinity,
    });
  }
});

$("#reset").addEventListener("click", async () => {
  if (!current || !confirm(`Reset ${FILES[method]} to the blank template? Your code in this file will be deleted.`)) return;
  clearTimeout(saveTimer);
  saveTimer = null;
  const { code } = await api(`/api/problems/${current.name}/reset`, { method: "POST", body: { method } });
  current.code[method] = code;
  editor.setValue(code);
  $("#save-state").textContent = "Saved";
});

// Method toggle: DataFrame API or Spark SQL. Each method has its own practice file.
const FILES = { dataframe: "practice_dataframe.py", sql: "practice_sql.py" };

function setMethod(m) {
  if (m === method && current) return;
  flushSave();
  method = m;
  store("method", m);
  $$("#method button").forEach((b) => b.classList.toggle("active", b.dataset.method === m));
  $("#lang").textContent = `Python · ${FILES[m]}`;
  $("#reset").title = `Reset ${FILES[m]} to the template`;
  if (current) showCode();
}

// Show the code of the selected method in the editor.
function showCode() {
  editor.setValue(current.code[method]);
  editor.clearHistory();
  $("#save-state").textContent = "Saved";
  setTimeout(() => editor.refresh(), 0);
}
$("#method").addEventListener("click", (e) => {
  const btn = e.target.closest("button");
  if (btn) setMethod(btn.dataset.method);
});
setMethod(method);

// ---------- Tables ----------

// A LeetCode-style text table. marks: {cols: Set, rows: Set, cls}.
function textTable(t, marks = null) {
  const widths = t.columns.map((c, i) => Math.max(c.length, ...t.rows.map((r) => r[i].length)));
  const line = (vals, rowMarked) => "| " + vals.map((v, i) => {
    const text = esc(v.padEnd(widths[i]));
    return marks && (rowMarked || marks.cols.has(i)) ? `<span class="${marks.cls}">${text}</span>` : text;
  }).join(" | ") + " |";
  return [
    line(t.columns, false),
    line(widths.map((w) => "-".repeat(w)), false),
    ...t.rows.map((r, i) => line(r, marks && marks.rows.has(i))),
  ].join("\n");
}

function box(name, t, marks) {
  return `<div class="box">${name ? `<span class="name">${esc(name)} =</span>` : ""}${textTable(t, marks)}</div>`;
}

function inputsHtml(inputs) {
  return `<div class="label">Input</div>` + Object.entries(inputs).map(([n, t]) => box(n, t)).join("");
}

function caseChips(count, active, mark = () => "") {
  return `<div class="case-chips">${Array.from({ length: count }, (_, i) =>
    `<button class="case-chip ${i === active ? "active" : ""}" data-case="${i}">${mark(i)}Case ${i + 1}</button>`).join("")}</div>`;
}

// ---------- Testcase tab ----------

function renderTestcases(active) {
  const cases = current.cases;
  const c = cases[active];
  $("#testcase").innerHTML = caseChips(cases.length, active)
    + inputsHtml(c.inputs)
    + `<div class="label">Expected</div>` + box("", c.expected);
}

$("#testcase").addEventListener("click", (e) => {
  const btn = e.target.closest(".case-chip");
  if (btn) renderTestcases(+btn.dataset.case);
});

// ---------- Run and Test Result tab ----------

async function run() {
  if (!current || $("#run").disabled) return;
  const name = current.name;
  clearTimeout(saveTimer);
  saveTimer = null;
  $("#run").disabled = true;
  $("#run").innerHTML = `<span class="spinner"></span>Running`;
  selectTab("test-panel", "result");
  $("#result").innerHTML = `<p class="placeholder"><span class="spinner"></span>Running ${method === "sql" ? "solve_sql()" : "solve()"}… Spark starts in a few seconds.</p>`;
  const started = performance.now();
  try {
    const data = await api(`/api/problems/${name}/run`, { method: "POST", body: { code: editor.getValue(), method } });
    $("#save-state").textContent = "Saved";
    if (current && current.name === name) {
      lastResult = { ...data, method, wall: performance.now() - started };
      renderResult(firstFailing(data.results));
    }
  } catch (err) {
    $("#result").innerHTML = `<div class="error-box">${esc(err.message)}</div>`;
  } finally {
    $("#run").disabled = false;
    $("#run").innerHTML = `${icon("Play")} Run`;
  }
}

$("#run").addEventListener("click", run);
document.addEventListener("keydown", (e) => {
  if ((e.metaKey || e.ctrlKey) && e.key === "Enter" && !$("#problem-page").hidden) { e.preventDefault(); run(); }
  if ((e.metaKey || e.ctrlKey) && e.key === "s" && !$("#problem-page").hidden) { e.preventDefault(); flushSave(); }
});

function firstFailing(results) {
  const i = results.findIndex((r) => r.status === "wrong" || r.status === "error");
  return Math.max(i, 0);
}

const MARK = {
  accepted: `<span class="mark ok">${icon("Check")}</span>`,
  wrong: `<span class="mark bad">${icon("X")}</span>`,
  error: `<span class="mark bad">${icon("X")}</span>`,
  skipped: `<span class="mark skip">${icon("Minus")}</span>`,
};

function verdict(results) {
  const has = (s) => results.some((r) => r.status === s);
  if (has("error")) return ["Runtime Error", "bad"];
  if (has("wrong")) return ["Wrong Answer", "bad"];
  if (results.every((r) => r.status === "skipped")) return ["Not Implemented", "skip"];
  if (has("skipped")) return ["Partly Implemented", "skip"];
  return ["Accepted", "ok"];
}

function renderResult(active) {
  const { results, errors, method: m } = lastResult;
  if (!results.length) {
    $("#result").innerHTML = `<div class="verdict bad"><h2>Compile Error</h2></div>`
      + `<div class="error-box">${esc(cleanError(errors.join("\n")))}</div>`;
    return;
  }
  const [title, cls] = verdict(results);
  const runtime = results.reduce((sum, r) => sum + (r.runtime_ms || 0), 0);
  const r = results[active];
  const fn = m === "sql" ? "solve_sql()" : "solve()";
  let html = `<div class="verdict ${cls}"><h2>${title}</h2>`
    + `<span class="muted">${fn}${cls === "ok" || title === "Wrong Answer" ? ` · Runtime: ${runtime} ms` : ""} · ${results.filter((x) => x.status === "accepted").length}/${results.length} passed</span></div>`
    + caseChips(results.length, active, (i) => MARK[results[i].status] || "");

  if (r.status === "skipped") {
    html += `<p class="muted"><code>${fn}</code> raises <code>NotImplementedError</code>. Write your answer in the editor, then run again.</p>`;
  }
  if (r.status === "error") {
    // The detail is the full message. Show it only when it has more than the first line.
    const more = r.detail && r.detail.trim().includes("\n");
    const text = more ? `${r.error.split(":")[0]}: ${cleanError(r.detail)}` : r.error;
    html += `<div class="error-box">${esc(text)}</div>`;
  }
  if (r.reason && r.reason.length) {
    html += r.reason.map((line) => `<div class="reason">${esc(line)}</div>`).join("");
  }
  html += inputsHtml(r.inputs);
  if (r.output) {
    html += `<div class="label">Output</div>` + box("", r.output, { cols: new Set(r.output.marked_cols), rows: new Set(r.output.marked_rows), cls: "cell-extra" });
    html += `<div class="label">Expected</div>` + box("", r.expected, { cols: new Set(r.expected.marked_cols), rows: new Set(r.expected.marked_rows), cls: "cell-missing" });
  }
  $("#result").innerHTML = html;
}

// Remove the JVM stack trace from Spark errors. Keep the useful first part.
function cleanError(text) {
  // A syntax error in a practice file stops the collection. Show only the pytest "E" lines.
  const start = text.search(/^E\s+File ".*practice_\w+\.py", line/m);
  if (start >= 0) {
    return text.slice(start).split("\n").filter((l) => l.startsWith("E ")).map((l) => l.slice(4)).join("\n");
  }
  const cut = text.search(/\n\s*(JVM stacktrace:|at org\.apache|at scala\.)/);
  return (cut > 0 ? text.slice(0, cut) : text).trim();
}

$("#result").addEventListener("click", (e) => {
  const btn = e.target.closest(".case-chip");
  if (btn && lastResult) renderResult(+btn.dataset.case);
});

// ---------- Resizable panels ----------

function dragGutter(gutter, onMove) {
  gutter.addEventListener("pointerdown", (e) => {
    e.preventDefault();
    gutter.setPointerCapture(e.pointerId);
    gutter.classList.add("dragging");
    document.body.classList.add("resizing");
    const move = (ev) => onMove(ev);
    const up = () => {
      gutter.removeEventListener("pointermove", move);
      gutter.removeEventListener("pointerup", up);
      gutter.classList.remove("dragging");
      document.body.classList.remove("resizing");
      if (editor) editor.refresh();
    };
    gutter.addEventListener("pointermove", move);
    gutter.addEventListener("pointerup", up);
  });
}

function setSplit(el, key, pct) {
  const clamped = Math.min(85, Math.max(15, pct));
  el.style.flexBasis = `${clamped}%`;
  store(key, String(clamped));
}

dragGutter($("#gutter-v"), (e) => {
  const box = $("#workspace").getBoundingClientRect();
  setSplit($("#left"), "split-v", ((e.clientX - box.left) / box.width) * 100);
});
dragGutter($("#gutter-h"), (e) => {
  const box = $("#right").getBoundingClientRect();
  setSplit($("#code-panel"), "split-h", ((e.clientY - box.top) / box.height) * 100);
  if (editor) editor.refresh();
});

for (const [id, key] of [["#left", "split-v"], ["#code-panel", "split-h"]]) {
  const saved = parseFloat(store(key));
  if (saved) $(id).style.flexBasis = `${saved}%`;
}

window.addEventListener("beforeunload", flushSave);
route();

// ---------- Spark settings ----------

let sparkDefaults = {};

function settingsRow(key = "", value = "") {
  const hint = key in sparkDefaults ? `Default: ${sparkDefaults[key]}` : "";
  return `<div class="settings-row">
    <input class="settings-key" placeholder="spark.some.key" value="${esc(key)}" spellcheck="false">
    <input class="settings-value" placeholder="value" value="${esc(value)}" title="${esc(hint)}" spellcheck="false">
    <button type="button" class="icon-btn settings-remove" title="Remove">${icon("Trash2")}</button>
  </div>`;
}

function renderSettings(config) {
  $("#settings-rows").innerHTML = Object.entries(config).map(([k, v]) => settingsRow(k, v)).join("");
  $("#settings-error").hidden = true;
}

function settingsError(message) {
  $("#settings-error").textContent = message;
  $("#settings-error").hidden = false;
}

$$(".settings-btn").forEach((btn) => btn.addEventListener("click", async () => {
  try {
    const data = await api("/api/spark-config");
    sparkDefaults = data.defaults;
    renderSettings(data.config);
    $("#settings").showModal();
  } catch (err) {
    alert(err.message);
  }
}));

$("#settings-add").addEventListener("click", () => {
  $("#settings-rows").insertAdjacentHTML("beforeend", settingsRow());
  $("#settings-rows .settings-row:last-child .settings-key").focus();
});

$("#settings-rows").addEventListener("click", (e) => {
  const btn = e.target.closest(".settings-remove");
  if (btn) btn.closest(".settings-row").remove();
});

$("#settings-defaults").addEventListener("click", () => renderSettings(sparkDefaults));
$("#settings-cancel").addEventListener("click", () => $("#settings").close());

$("#settings-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const config = {};
  for (const row of $$("#settings-rows .settings-row")) {
    const key = row.querySelector(".settings-key").value.trim();
    const value = row.querySelector(".settings-value").value.trim();
    if (!key && !value) continue;
    if (!key) return settingsError(`The value "${value}" has no key.`);
    if (key in config) return settingsError(`The key ${key} is in the list two times.`);
    config[key] = value;
  }
  try {
    await api("/api/spark-config", { method: "PUT", body: { config } });
    $("#settings").close();
  } catch (err) {
    settingsError(err.message);
  }
});

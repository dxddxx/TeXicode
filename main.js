async function main() {
  const input = document.getElementById("input");
  const output = document.getElementById("output");
  const fontToggle = document.getElementById("font-toggle");
  const demoTex = input.placeholder;

  output.disabled = true;
  output.value = "Loading Pyodide...";

  const pyodide = await loadPyodide();

  output.value = "Loading TeXicode...";
  const files = [
    "texicode/arts.py",
    "texicode/lexer.py",
    "texicode/main.py",
    "texicode/node_data.py",
    "texicode/parser.py",
    "texicode/pipeline.py",
    "texicode/renderer.py",
    "texicode/symbols_art.py",
  ];

  // ensure package directory exists in Pyodide FS
  try {
    pyodide.FS.mkdir('texicode');
  } catch (e) {
    // ignore if already exists
  }

  for (const f of files) {
    const resp = await fetch(`./src/${f}`);
    pyodide.FS.writeFile(f, await resp.text());
  }

  // Some static hosts omit __init__.py; fall back to a shim if missing.
  try {
    const respInit = await fetch('./src/texicode/__init__.py');
    if (respInit.ok) {
      pyodide.FS.writeFile('texicode/__init__.py', await respInit.text());
    } else {
      pyodide.FS.writeFile('texicode/__init__.py', 'from .main import main\n');
    }
  } catch (e) {
    pyodide.FS.writeFile('texicode/__init__.py', 'from .main import main\n');
  }

  output.value = "Preparing TeXicode...";
  await pyodide.runPythonAsync(`
import sys, importlib
sys.path.insert(0, "")
mod = importlib.import_module("texicode.pipeline")
render_tex_web = mod.render_tex_web
  `);

  input.disabled = false;
  output.disabled = false;
  output.value = "";
  let isNormalFont = false;

  let editor;
  if (typeof CodeMirror !== 'undefined') {
    editor = CodeMirror.fromTextArea(input, {
      mode: 'stex',
      theme: 'dracula',
      keyMap: 'vim',
      placeholder: input.placeholder,
      lineWrapping: true,
      showCursorWhenSelecting: true,
      lineNumbers: false,
      viewportMargin: Infinity,
      extraKeys: { 'Ctrl-S': async () => { await updateOutput(); } }
    });

    editor.setSize('100%', '100%');
    // Keep the editor in sync with the app theme.
    try {
      editor.getWrapperElement().classList.add('cm-s-dracula');
      editor.setOption('theme', 'dracula');
      editor.refresh();
    } catch (e) {}

    // Vim mode starts in insert mode.
    setTimeout(() => {
      try {
        if (editor.getOption('keyMap') === 'vim' && typeof CodeMirror.Vim !== 'undefined') {
          CodeMirror.Vim.handleKey(editor, 'i');
        }
      } catch (e) {}
    }, 50);
  }

  // CodeMirror's block cursor is empty; draw the character under the cursor
  // inside it, otherwise the letter is invisible on the white block.
  function syncFatCursorText() {
    if (!editor) return;
    try {
      const wrapper = editor.getWrapperElement();
      if (!wrapper.classList.contains('cm-fat-cursor')) return;
      const pos = editor.getCursor();
      const line = editor.getLine(pos.line) || "";
      const codePoint = line.codePointAt(pos.ch);
      const ch = codePoint === undefined ? " " : String.fromCodePoint(codePoint);
      for (const el of wrapper.querySelectorAll(".CodeMirror-cursor")) {
        if (el.textContent !== ch) el.textContent = ch;
      }
    } catch (e) {}
  }

  if (editor) {
    editor.on("cursorActivity", syncFatCursorText);
    editor.on("update", syncFatCursorText);
    editor.on("focus", syncFatCursorText);

    // Escape does not always move the cursor, so sync right away.
    editor.getInputField().addEventListener("keydown", (e) => {
      if (e.key === "Escape") setTimeout(syncFatCursorText, 0);
    });

    // Re-fill the cursor whenever CodeMirror redraws it as a blank box.
    const wrapper = editor.getWrapperElement();
    const cursorObserver = new MutationObserver(syncFatCursorText);
    cursorObserver.observe(wrapper, {
      childList: true,
      subtree: true,
      characterData: true,
    });

    setTimeout(syncFatCursorText, 100);
  }

  async function updatePlaceholder() {
    const placeholder = await pyodide.runPythonAsync(
      `render_tex_web(${JSON.stringify(demoTex)}, ${isNormalFont ? "True" : "False"})`
    );
    output.placeholder = placeholder ?? "";
  }

  await updatePlaceholder();

  fontToggle.addEventListener("change", async () => {
    isNormalFont = fontToggle.checked;
    await updatePlaceholder();
    updateOutput();
  });

  let timeoutId;
  if (editor) {
    editor.on('change', () => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(updateOutput, 0);
    });
  } else {
    input.addEventListener("input", () => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(updateOutput, 0);
    });
  }

  async function updateOutput() {
    try {
      const currentText = editor ? editor.getValue() : input.value;
      const result = await pyodide.runPythonAsync(
        `render_tex_web(${JSON.stringify(currentText)}, ${isNormalFont ? "True" : "False"})`
      );

      output.value = result ?? "";
    } catch (err) {
      output.value = "Error: " + err;
      console.error(err);
    }
  }

  for (const [btnId, txtId] of [
    ["copy-input", "input"],
    ["copy-output", "output"],
  ]) {
    const btn = document.getElementById(btnId);
    const txt = document.getElementById(txtId);
    btn.addEventListener("click", async () => {
      let textToCopy = txt.value;
      if (btnId === 'copy-input' && editor) {
        textToCopy = editor.getValue();
      }
      await navigator.clipboard.writeText(textToCopy);
      btn.textContent = "Copied!";
      setTimeout(() => (btn.textContent = "Copy"), 1500);
    });
  }
}

main();

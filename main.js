async function main() {
  // Original textarea elements
  const input = document.getElementById("input");
  const output = document.getElementById("output");
  const fontToggle = document.getElementById("font-toggle");
  const demoTex = input.placeholder;

  // input.disabled = true;
  output.disabled = true;
  output.value = "Loading Pyodide...";

  const pyodide = await loadPyodide();

  output.value = "Loading TeXicode...";
  const files = [
    "texicode/__init__.py",
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
    const code = await resp.text();
    // write into the same path inside the virtual FS so package-relative imports work
    pyodide.FS.writeFile(f, code);
  }

  try {
    const respInit = await fetch('./src/texicode/__init__.py');
    if (respInit.ok) {
      const initCode = await respInit.text();
      pyodide.FS.writeFile('texicode/__init__.py', initCode);
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
      showCursorWhenSelecting: true,
      lineNumbers: false,
      viewportMargin: Infinity,
      extraKeys: { 'Ctrl-S': async () => { await updateOutput(); } }
    });

    editor.setSize('100%', '100%');
    // Ensure theme class is present and refresh the editor
    try {
      editor.getWrapperElement().classList.add('cm-s-dracula');
      editor.setOption('theme', 'dracula');
      editor.refresh();
    } catch (e) {}

    // Enter insert mode by default
    setTimeout(() => {
      try {
        if (editor.getOption('keyMap') === 'vim' && typeof CodeMirror.Vim !== 'undefined') {
          CodeMirror.Vim.handleKey(editor, 'i');
        }
      } catch (e) {}
    }, 50);
  }

  async function updatePlaceholder() {
    const placeholder = await pyodide.runPythonAsync(
      `render_tex_web(${JSON.stringify(demoTex)}, ${isNormalFont ? "True" : "False"})`
    );
    output.placeholder = placeholder ?? "";
  }

  // NEW: call once after load
  await updatePlaceholder();

  // listen for font toggle
  fontToggle.addEventListener("change", async () => {
    isNormalFont = fontToggle.checked;
    await updatePlaceholder();
    updateOutput();  // re-render immediately
  });

  // listen for input change
  let timeoutId;
  // Use CodeMirror change event when available; fall back to textarea input
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
      // const result = await pyodide.runPythonAsync(
      //   `render_tex_web(${JSON.stringify(input.value)})`
      // );
      const currentText = editor ? editor.getValue() : input.value;
      const texString = JSON.stringify(currentText);

      const result = await pyodide.runPythonAsync(
        `render_tex_web(${texString}, ${isNormalFont ? "True" : "False"})`
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
      // for copy-input, use CodeMirror content if available
      let textToCopy = txt.value;
      if (btnId === 'copy-input' && editor) {
        textToCopy = editor.getValue();
      }
      await navigator.clipboard.writeText(textToCopy);
      const orig = btn.textContent;
      btn.textContent = "Copied!";
      setTimeout(() => (btn.textContent = "Copy"), 1500);
    });
  }
}

main();

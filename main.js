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

  // Ensure __init__.py is available to Python package import. Many static hosts
  // occasionally omit directory index files; attempt to fetch the real file,
  // otherwise write a small shim into the Pyodide FS so package-relative
  // imports work.
  try {
    const respInit = await fetch('./src/texicode/__init__.py');
    if (respInit.ok) {
      const initCode = await respInit.text();
      pyodide.FS.writeFile('texicode/__init__.py', initCode);
      console.log('TeXicode: wrote __init__.py from server');
    } else {
      // fallback shim
      pyodide.FS.writeFile('texicode/__init__.py', 'from .main import main\n');
      console.warn('TeXicode: __init__.py missing on server — wrote shim fallback');
    }
  } catch (e) {
    pyodide.FS.writeFile('texicode/__init__.py', 'from .main import main\n');
    console.warn('TeXicode: error fetching __init__.py — wrote shim fallback', e);
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

  // Initialize CodeMirror on the input textarea with Vim keymap and monochrome theme
  let editor;
  if (typeof CodeMirror !== 'undefined') {
    editor = CodeMirror.fromTextArea(input, {
      mode: 'stex',
      theme: 'monochrome',
      keyMap: 'vim',
      lineNumbers: false,
      viewportMargin: Infinity,
      extraKeys: { 'Ctrl-S': async () => { await updateOutput(); } }
    });

    // Mirror font toggle and placeholder behavior to the CodeMirror editor
    editor.setSize(null, 160);
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
      await navigator.clipboard.writeText(txt.value);
      const orig = btn.textContent;
      btn.textContent = "Copied!";
      setTimeout(() => (btn.textContent = "Copy"), 1500);
    });
  }
}

main();

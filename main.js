async function main() {
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
    "arts.py", "lexer.py", "main.py",
    "node_data.py", "parser.py", "pipeline.py",
    "renderer.py", "symbols_art.py",
  ];

  for (const f of files) {
    const resp = await fetch(`./src/${f}`);
    const code = await resp.text();
    pyodide.FS.writeFile(f, code);
  }

  output.value = "Preparing TeXicode...";
  await pyodide.runPythonAsync(`
import sys, runpy
sys.path.insert(0, "")
mod = runpy.run_path("pipeline.py")
render_tex_web = mod["render_tex_web"]
  `);

  input.disabled = false;
  output.disabled = false;
  output.value = "";
  let isNormalFont = false;

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
  input.addEventListener("input", () => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(updateOutput, 0);
  });

  async function updateOutput() {
    try {
      // const result = await pyodide.runPythonAsync(
      //   `render_tex_web(${JSON.stringify(input.value)})`
      // );
      const texString = JSON.stringify(input.value);

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

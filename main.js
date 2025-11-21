async function main() {
  const input = document.getElementById("input");
  const output = document.getElementById("output");

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

  let timeoutId;
  input.addEventListener("input", () => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(updateOutput, 0);
  });

  async function updateOutput() {
    try {
      const result = await pyodide.runPythonAsync(
        `render_tex_web(${JSON.stringify(input.value)})`
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

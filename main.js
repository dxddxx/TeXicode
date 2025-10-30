async function main() {
  const pyodide = await loadPyodide();

  const files = [
    "arts.py", "lexer.py", "main.py", "node_data.py",
    "parser.py", "pipeline.py", "renderer.py", "symbols_art.py",
  ];

  for (const f of files) {
    const resp = await fetch(`./src/${f}`);
    const code = await resp.text();
    pyodide.FS.writeFile(f, code);
  }

  // Load Python entry point
  await pyodide.runPythonAsync(`
import sys, runpy
sys.path.insert(0, "")
mod = runpy.run_path("pipeline.py")
render_tex_web = mod["render_tex_web"]
  `);

  const input = document.getElementById("input");
  const output = document.getElementById("output");

  let timeoutId;
  input.addEventListener("input", () => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(updateOutput, 0);
  });

  async function updateOutput() {
    const text = input.value;
    try {
      const result = await pyodide.runPythonAsync(
        "render_tex_web(" + JSON.stringify(text) + ")"
      );
      output.value = result ?? "";
    } catch (err) {
      output.value = "Error: " + err;
      console.error(err);
    }
  }

  // Copy button support
  function addCopyHandler(id, getTextFn, baseLabel) {
    const el = document.getElementById(id);
    el.addEventListener("click", async () => {
      if (!navigator.clipboard) return;
      try {
        await navigator.clipboard.writeText(getTextFn());
        const original = el.textContent;
        el.textContent = "Copied!";
        setTimeout(() => {
          el.textContent = baseLabel;
        }, 1000);
      } catch (e) {
        console.error("Clipboard error", e);
      }
    });
  }

  addCopyHandler("copy-input", () => input.value, "Copy Input");
  addCopyHandler("copy-output", () => output.value, "Copy Output");
}

main();

import { loadMicroPython } from "./build-standard/micropython.mjs";

async function main() {
  const input = document.getElementById("input");
  const output = document.getElementById("output");
  input.disabled = true;
  output.disabled = true;
  output.value = "Loading MicroPython...";

  // No stdout handler needed
  const mp = await loadMicroPython();

  // Load files (same as before)
  const pyFiles = ["arts.py", "lexer.py", "main.py", "node_data.py",
                   "parser.py", "pipeline.py", "renderer.py", "symbols_art.py"];
  for (const f of pyFiles) {
    const txt = await (await fetch(`./src/${f}`)).text();
    mp.FS.writeFile(f, txt);
  }

  // Import function
  await mp.runPythonAsync(`
import sys
sys.path.insert(0, "")
import pipeline
render_tex_web = pipeline.render_tex_web
  `);

  input.disabled = false;
  output.disabled = false;
  output.value = "";

  let updateTimer;
  input.addEventListener("input", () => {
    clearTimeout(updateTimer);
    updateTimer = setTimeout(updateOutput, 0);
  });

  // Synchronous, direct return
  function updateOutput() {
    try {
      const result = mp.runPython(`render_tex_web(${JSON.stringify(input.value)})`);
      output.value = result ?? "";
    } catch (err) {
      output.value = "Error: " + err;
    }
  }

  // Copy buttons (unchanged)
  for (const [btnId, txtId] of [["copy-input", "input"], ["copy-output", "output"]]) {
    const btn = document.getElementById(btnId);
    const txt = document.getElementById(txtId);
    btn.addEventListener("click", async () => {
      await navigator.clipboard.writeText(txt.value);
      btn.textContent = "Copied!";
      setTimeout(() => btn.textContent = "Copy", 1500);
    });
  }
}

main();

import { loadMicroPython } from "./build-standard/micropython.mjs";

async function main() {
  const input  = document.getElementById("input");
  const output = document.getElementById("output");
  input.disabled = true;
  output.disabled = true;
  output.value = "Loading MicroPython...";

  // --- 1. Start MicroPython environment ---
  const mp = await loadMicroPython();

  // --- 2. Load your Python source files into the virtual FS ---
  const pyFiles = [
    "arts.py", "lexer.py", "main.py", "node_data.py",
    "parser.py", "pipeline.py", "renderer.py", "symbols_art.py",
  ];
  for (const f of pyFiles) {
    const resp = await fetch(`./src/${f}`);
    const code = await resp.text();
    mp.FS.writeFile(f, code);
  }

  // --- 3. Import your pipeline and expose render_tex_web ---
  await mp.runPythonAsync(`
import sys
sys.path.insert(0, "")
import pipeline
render_tex_web = pipeline.render_tex_web
`);

  input.disabled = false;
  output.disabled = false;
  output.value = "";

  // --- 4. Update output whenever input changes ---
  let timer;
  input.addEventListener("input", () => {
    clearTimeout(timer);
    timer = setTimeout(updateOutput, 0);
  });

  async function updateOutput() {
    try {
      const code = `
from pipeline import render_tex_web
render_tex_web(${JSON.stringify(input.value)})
`;
      const result = await mp.runPythonAsync(code);
      output.value = result ?? "";
    } catch (err) {
      output.value = "Error: " + err;
      console.error(err);
    }
  }

  // --- 5. Copy buttons ---
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
      setTimeout(() => (btn.textContent = orig), 1500);
    });
  }
}

main();

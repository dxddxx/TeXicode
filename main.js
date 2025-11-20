import { loadMicroPython } from "./build-standard/micropython.mjs";

async function main() {
  const input  = document.getElementById("input");
  const output = document.getElementById("output");
  input.disabled = true;
  output.disabled = true;
  output.value = "Loading MicroPython...";

  // --- 1. Start MicroPython runner ---
  const stdoutWriter = (line) => { console.log(line); };
  const mp = await loadMicroPython({ stdout: stdoutWriter });

  // --- 2. Load Python source files into MP’s virtual FS ---
  const pyFiles = [
    "arts.py", "lexer.py", "main.py", "node_data.py",
    "parser.py", "pipeline.py", "renderer.py", "symbols_art.py",
  ];

  for (const f of pyFiles) {
    const txt = await (await fetch(`./src/${f}`)).text();
    mp.FS.writeFile(f, txt);
  }

  // --- 3. Import your pipeline & exporter function ---
  await mp.runPythonAsync(`
import sys, runpy
sys.path.insert(0, "")
mod = runpy.run_path("pipeline.py")
render_tex_web = mod["render_tex_web"]
  `);

  input.disabled = false;
  output.disabled = false;
  output.value = "";

  // --- 4. Bind update logic just like before ---
  let updateTimer;
  input.addEventListener("input", () => {
    clearTimeout(updateTimer);
    updateTimer = setTimeout(updateOutput, 0);
  });

  async function updateOutput() {
    try {
      const code = `print(render_tex_web(${JSON.stringify(input.value)}))`;
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
      setTimeout(() => (btn.textContent = "Copy"), 1500);
    });
  }
}

main();

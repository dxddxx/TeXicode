// main.js - Debug Version
import { loadMicroPython } from "./build-standard/micropython.mjs";

async function main() {
  const input = document.getElementById("input");
  const output = document.getElementById("output");
  input.disabled = true;
  output.disabled = true;
  output.value = "Loading MicroPython...";

  // 1. Create buffer to capture stdout with debug logging
  let outputBuffer = "";
  const mp = await loadMicroPython({
    stdout: (line) => {
      console.log("STDOUT CAPTURED:", JSON.stringify(line));
      outputBuffer += line + "\n";
    }
  });
  console.log("MicroPython loaded successfully");

  // 2. Load Python files with error checking
  const pyFiles = [
    "arts.py", "lexer.py", "main.py", "node_data.py",
    "parser.py", "pipeline.py", "renderer.py", "symbols_art.py",
  ];
  
  for (const f of pyFiles) {
    try {
      const resp = await fetch(`./src/${f}`);
      if (!resp.ok) throw new Error(`HTTP ${resp.status} for ${f}`);
      const txt = await resp.text();
      mp.FS.writeFile(f, txt);
      console.log(`Loaded ${f} (${txt.length} chars)`);
    } catch (err) {
      console.error(`Failed to load ${f}:`, err);
      output.value = `Failed to load ${f}: ${err}`;
      return;
    }
  }

  // 3. Import the function with debug
  try {
    await mp.runPythonAsync(`
import sys
sys.path.insert(0, "")
# print("DEBUG: About to import pipeline")
import pipeline
# print("DEBUG: pipeline imported successfully")
# print("DEBUG: render_tex_web exists:", hasattr(pipeline, 'render_tex_web'))
render_tex_web = pipeline.render_tex_web
    `);
    console.log("Python setup completed");
  } catch (err) {
    console.error("Python setup failed:", err);
    output.value = "Setup error: " + err;
    return;
  }

  input.disabled = false;
  output.disabled = false;
  output.value = "";

  let updateTimer;
  input.addEventListener("input", () => {
    clearTimeout(updateTimer);
    updateTimer = setTimeout(updateOutput, 0);
  });

  async function updateOutput() {
    console.log("\n=== updateOutput called ===");
    console.log("Input value:", JSON.stringify(input.value));
    
    try {
      outputBuffer = "";
      console.log("Buffer cleared");
      
      const pythonCode = `
# print("DEBUG: Starting render_tex_web")
result = render_tex_web(${JSON.stringify(input.value)})
# print("DEBUG: render_tex_web finished, result type:", type(result))
# print("DEBUG: result value:", repr(result) if result else "None")
print(result)  # This is what should go to stdout
# print("DEBUG: After printing result")
      `;
      
      console.log("Running Python code...");
      await mp.runPythonAsync(pythonCode);
      
      console.log("Python execution finished");
      console.log("Buffer contents:", JSON.stringify(outputBuffer));
      console.log("Buffer length:", outputBuffer.length);
      
      output.value = outputBuffer.trimEnd();
      console.log("Output textarea updated");
      
    } catch (err) {
      console.error("ERROR in updateOutput:", err);
      output.value = "Error: " + err;
    }
  }

  // 5. Copy buttons (unchanged)
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

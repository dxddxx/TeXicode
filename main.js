import { loadMicroPython } from "./build-standard/micropython.mjs";

async function main() {
  console.log("=== main() started ===");
  const input = document.getElementById("input");
  const output = document.getElementById("output");
  
  console.log("Input element:", input);
  console.log("Output element:", output);
  
  input.disabled = true;
  output.value = "Loading...";
  console.log("Set output to 'Loading...'");

  try {
    console.log("Loading MicroPython...");
    const mp = await loadMicroPython();
    console.log("✓ MicroPython loaded:", mp);

    // Load all Python files
    const files = ["arts.py", "lexer.py", "main.py", "node_data.py", 
                   "parser.py", "pipeline.py", "renderer.py", "symbols_art.py"];
    console.log("Files to load:", files);
    
    for (const f of files) {
      console.log(`Fetching ${f}...`);
      const resp = await fetch(`./src/${f}`);
      console.log(`Response status for ${f}:`, resp.status);
      const txt = await resp.text();
      console.log(`Content of ${f}:`, txt.substring(0, 100) + "...");
      mp.FS.writeFile(f, txt);
      console.log(`✓ Wrote ${f} to virtual FS`);
    }

    // Create wrapper
    console.log("Creating Python wrapper...");
    await mp.runPythonAsync(`
import sys, pipeline
def _render_wrapper(tex):
    try:
        result = pipeline.render_tex_web(tex)
        return str(result) if result is not None else ""
    except Exception as e:
        return f"Error: {e}"
    `);
    console.log("✓ Wrapper created");

    input.disabled = false;
    output.value = "";
    console.log("✓ UI ready");

    let timer;
    input.addEventListener("input", () => {
      console.log("\n=== Input event fired ===");
      clearTimeout(timer);
      timer = setTimeout(update, 100);
    });

    function update() {
      console.log("\n=== update() called ===");
      const currentInput = input.value;
      console.log("Input value:", JSON.stringify(currentInput));
      
      try {
        const pythonCode = `_render_wrapper(${JSON.stringify(currentInput)})`;
        console.log("Python code to execute:", pythonCode);
        
        const result = mp.runPython(pythonCode);
        console.log("Raw result from runPython:", result);
        console.log("Result type:", typeof result);
        console.log("Result == null:", result === null);
        console.log("Result == undefined:", result === undefined);
        
        output.value = result ?? "";
        console.log("Output textarea updated to:", JSON.stringify(output.value));
      } catch (err) {
        console.error("Error in update():", err);
        output.value = "JS Error: " + err;
      }
    }

    // Copy buttons
    console.log("Setting up copy buttons...");
    for (const [btnId, txtId] of [["copy-input", "input"], ["copy-output", "output"]]) {
      const btn = document.getElementById(btnId);
      const txt = document.getElementById(txtId);
      btn.addEventListener("click", async () => {
        await navigator.clipboard.writeText(txt.value);
        btn.textContent = "Copied!";
        setTimeout(() => btn.textContent = "Copy", 1500);
      });
    }
    console.log("✓ Copy buttons ready");

  } catch (err) {
    console.error("Fatal error:", err);
    output.value = "Fatal: " + err;
  }
}

main().catch(err => console.error("main() failed:", err));

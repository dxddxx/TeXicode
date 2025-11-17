async function main() {
  const pyodide = await loadPyodide();
  const files = [
    "arts.py", "lexer.py", "main.py", "node_data.py",
    "parser.py", "pipeline.py", "renderer.py", "symbols_art.py"
  ];
  
  for (const f of files) {
    const resp = await fetch(`./src/${f}`);
  pyodide.FS.writeFile(f, await resp.text());
  }
  
  await pyodide.runPythonAsync(`
import sys, runpy
sys.path.insert(0, "")
mod = runpy.run_path("pipeline.py");
render_tex_web = mod["render_tex_web"];
`);
  
  const input = document.getElementById("input");
  const output = document.getElementById("output");
  let timeoutId;
  
  input.addEventListener("input", () => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(updateOutput, 0);
  });
  
  async function updateOutput() {
    try {
      output.value = await pyodide.runPythonAsync(
        `render_tex_web(${JSON.stringify(input.value)})`
    );
  } catch (err) {
    output.value = "Error: " + err;
  }
}
  
// Copy buttons
document.getElementById("copy-input").addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(input.value);
  const btn = document.getElementById("copy-input");
  btn.textContent = "Copied!";
  setTimeout(() => btn.textContent = "Copy", 1500);
});

document.getElementById("copy-output").addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(output.value);
  const btn = document.getElementById("copy-output");
  btn.textContent = "Copied!";
  setTimeout(() => btn.textContent = "Copy", 1500);
});
}

main();

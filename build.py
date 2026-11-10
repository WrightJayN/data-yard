"""Build index.html: inline sql.js + its WebAssembly so the game is one offline file."""
import base64, pathlib
root = pathlib.Path(__file__).parent
dist = root / "node_modules" / "sql.js" / "dist"
src = (root / "src" / "game.html").read_text()
js = (dist / "sql-wasm.js").read_text()
wasm = base64.b64encode((dist / "sql-wasm.wasm").read_bytes()).decode()
out = src.replace("/*__SQLJS__*/", js, 1).replace("/*__WASM__*/", wasm, 1)
(root / "index.html").write_text(out)
print(f"index.html written ({len(out)//1024} KB)")

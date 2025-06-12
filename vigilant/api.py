from fastapi import FastAPI
from pathlib import Path
from .scanners.secrets.scanner import scan_path

app = FastAPI(title="Vigilant Scanner")

@app.get("/health")
def health():
    return {"status":"ok"}

@app.get("/scan")
def scan(path: str = "."):
    findings = scan_path(Path(path))
    return {"count": len(findings), "findings": findings[:20]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

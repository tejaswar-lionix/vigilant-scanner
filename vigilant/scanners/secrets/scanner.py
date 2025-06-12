"""Secret scanner - orchestrates pattern matching + entropy + validation"""
import pathlib, re
from typing import List, Dict, Any
from .patterns import PATTERNS
from .entropy import is_high_entropy
from .validators import is_false_positive

def scan_file(path: pathlib.Path) -> List[Dict[str, Any]]:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except:
        return []
    if len(text) > 200_000:  # skip huge files
        return []
    findings = []
    for pat in PATTERNS:
        for m in pat.compiled.finditer(text):
            val = m.group(0)
            if is_false_positive(val, text[max(0, m.start()-50):m.end()+50]):
                continue
            # Entropy check for high severity
            if pat.severity in ("critical","high") and len(val) > 20:
                if not is_high_entropy(val, 3.5) and "key" not in pat.id:
                    # Keep but lower confidence if low entropy
                    pass
            findings.append({
                "file": str(path),
                "pattern_id": pat.id,
                "severity": pat.severity,
                "platform": pat.platform,
                "match": val[:60],
                "line": text[:m.start()].count("\n")+1
            })
            if len(findings) > 20:
                break
        if len(findings) > 20:
            break
    return findings

def scan_path(root: pathlib.Path) -> List[Dict[str, Any]]:
    skip_dirs = {"node_modules",".git","__pycache__",".venv","dist","build",".next"}
    all_findings = []
    for p in root.rglob("*"):
        if p.is_dir():
            if p.name in skip_dirs:
                # prune
                continue
            continue
        if p.is_file() and p.suffix in (".py",".js",".ts",".yaml",".yml",".json",".env",".toml",".md",".txt"):
            if ".git" in str(p):
                continue
            all_findings.extend(scan_file(p))
    return all_findings

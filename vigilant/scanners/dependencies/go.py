"""Go audit - parse go.mod"""
import pathlib, re
from typing import List, Dict, Any

def parse_go_mod(path: pathlib.Path):
    deps={}
    for line in path.read_text(errors="ignore").splitlines():
        m=re.match(r"\s+([a-zA-Z0-9/._-]+)\s+v([0-9.]+)", line)
        if m:
            deps[m.group(1)]=m.group(2)
    return deps

def audit_go(root: pathlib.Path):
    findings=[]
    for p in root.rglob("go.mod"):
        deps=parse_go_mod(p)
        for pkg,ver in deps.items():
            if "golang.org/x/net" in pkg and ver < "0.7.0":
                findings.append({"file":str(p),"pkg":pkg,"version":ver,"cve":"CVE-2022-27664"})
    return findings

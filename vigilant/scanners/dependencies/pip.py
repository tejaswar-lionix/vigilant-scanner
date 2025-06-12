"""pip audit - parse requirements.txt and check advisories"""
import pathlib, re
from typing import List, Dict, Any

def parse_requirements(path: pathlib.Path) -> Dict[str, str]:
    deps = {}
    for line in path.read_text(errors="ignore").splitlines():
        line=line.strip()
        if not line or line.startswith("#"):
            continue
        m=re.match(r"([a-zA-Z0-9_-]+)\s*==\s*([0-9.]+)", line)
        if m:
            deps[m.group(1).lower()]=m.group(2)
        else:
            m=re.match(r"([a-zA-Z0-9_-]+)", line)
            if m:
                deps[m.group(1).lower()]="*"
    return deps

def check_pip_advisory(pkg: str, version: str):
    db={"django":[{"cve":"CVE-2022-34265","severity":"critical","fixed":"3.2.15"}],"requests":[{"cve":"CVE-2023-32681","severity":"medium","fixed":"2.31.0"}]}
    return db.get(pkg, [])

def audit_pip(root: pathlib.Path):
    findings=[]
    for p in root.rglob("requirements*.txt"):
        deps=parse_requirements(p)
        for pkg,ver in deps.items():
            for adv in check_pip_advisory(pkg, ver):
                if ver != adv["fixed"] and ver != "*":
                    findings.append({"file":str(p),"pkg":pkg,"version":ver,"advisory":adv})
    return findings

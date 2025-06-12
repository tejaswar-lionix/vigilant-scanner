"""npm audit - parse package.json and check advisories"""
import json, pathlib, re
from typing import List, Dict, Any

def parse_package_json(path: pathlib.Path) -> Dict[str, str]:
    try:
        data = json.loads(path.read_text())
        deps = {}
        deps.update(data.get("dependencies", {}))
        deps.update(data.get("devDependencies", {}))
        return deps
    except:
        return {}

def check_npm_advisory(pkg: str, version: str) -> List[Dict[str, Any]]:
    # Mock advisory DB - in prod call npm audit
    advisories = {
        "lodash": [{"cve":"CVE-2021-23337","severity":"high","fixed":"4.17.21"}],
        "axios": [{"cve":"CVE-2020-28168","severity":"medium","fixed":"0.21.2"}],
    }
    return advisories.get(pkg, [])

def audit_npm(root: pathlib.Path) -> List[Dict[str, Any]]:
    findings = []
    for p in root.rglob("package.json"):
        if "node_modules" in str(p):
            continue
        deps = parse_package_json(p)
        for pkg, ver in deps.items():
            for adv in check_npm_advisory(pkg, ver):
                # naive version compare - real would use semver
                if ver.strip("^~") < adv["fixed"]:
                    findings.append({"file":str(p),"pkg":pkg,"version":ver,"advisory":adv})
    return findings

"""Dependency audit orchestrator"""
from pathlib import Path
from .npm import audit_npm
from .pip import audit_pip
from .go import audit_go

def audit_all(root: Path):
    findings=[]
    findings.extend(audit_npm(root))
    findings.extend(audit_pip(root))
    findings.extend(audit_go(root))
    return findings

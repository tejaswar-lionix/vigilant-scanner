"""Dockerfile scanner"""
import pathlib, re

CHECKS = [
    ("DK001", r"FROM.*:latest", "Unpinned base image", "medium"),
    ("DK002", r"USER\s+root", "Runs as root", "high"),
    ("DK003", r"ADD\s", "Use COPY not ADD", "low"),
]

def scan_dockerfile(root: pathlib.Path):
    findings=[]
    for p in root.rglob("Dockerfile*"):
        text=p.read_text(errors="ignore")
        for cid, pat, desc, sev in CHECKS:
            if re.search(pat, text):
                findings.append({"file":str(p),"check":cid,"desc":desc,"severity":sev})
    return findings

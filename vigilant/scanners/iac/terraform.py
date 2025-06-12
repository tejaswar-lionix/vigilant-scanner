"""Terraform misconfig scanner"""
import pathlib, re
from typing import List, Dict, Any

CHECKS = [
    ("TF001", r's3_bucket.*acl.*public', "S3 bucket public ACL", "critical"),
    ("TF002", r'cidr.*0\.0\.0\.0/0', "Open CIDR", "high"),
    ("TF003", r'ingress.*from_port.*0', "Open ingress", "high"),
]

def scan_terraform(root: pathlib.Path):
    findings=[]
    for p in root.rglob("*.tf"):
        text=p.read_text(errors="ignore")
        for cid, pat, desc, sev in CHECKS:
            if re.search(pat, text):
                findings.append({"file":str(p),"check":cid,"desc":desc,"severity":sev})
    return findings

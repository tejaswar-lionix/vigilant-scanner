"""K8s manifest scanner"""
import pathlib, re

def scan_k8s(root: pathlib.Path):
    findings=[]
    for p in root.rglob("*.yaml"):
        text=p.read_text(errors="ignore")
        if "privileged: true" in text:
            findings.append({"file":str(p),"check":"K8S001","desc":"Privileged container","severity":"critical"})
        if "hostNetwork: true" in text:
            findings.append({"file":str(p),"check":"K8S002","desc":"hostNetwork true","severity":"high"})
        if "runAsUser: 0" in text:
            findings.append({"file":str(p),"check":"K8S003","desc":"Runs as root","severity":"high"})
    return findings

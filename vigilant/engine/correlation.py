"""Correlation - group findings by file and type, deduplicate by hash"""
import hashlib, json

def dedupe(findings):
    seen=set()
    out=[]
    for f in findings:
        h=hashlib.md5(json.dumps({k:f[k] for k in sorted(f) if k!="line"}, sort_keys=True).encode()).hexdigest()
        if h not in seen:
            seen.add(h)
            out.append(f)
    return out

def correlate(secrets, deps, iac):
    # Group by file, prioritize critical
    all_findings = secrets + deps + iac
    # Sort by severity
    rank={"low":1,"medium":2,"high":3,"critical":4}
    all_findings.sort(key=lambda x: rank.get(x.get("severity","medium"),2), reverse=True)
    return dedupe(all_findings)

"""Dedupe - file+line+pattern dedup, window 5min for logs"""
import time, hashlib

def dedupe_by_window(findings, window=300):
    # For log findings, dedupe within window
    seen={}
    out=[]
    for f in findings:
        key=(f.get("file"), f.get("pattern_id"))
        now=time.time()
        if key not in seen or now - seen[key] > window:
            seen[key]=now
            out.append(f)
    return out

"""Hashing helpers - file hashing, not repetitive clones"""
import hashlib, pathlib

def sha256_file(path: pathlib.Path) -> str:
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def short_hash(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()[:8]

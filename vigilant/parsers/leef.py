"""LEEF parser"""
import re
def parse_leef(line: str):
    if not line.startswith("LEEF:"):
        return None
    return {"format":"LEEF","raw":line[:100]}

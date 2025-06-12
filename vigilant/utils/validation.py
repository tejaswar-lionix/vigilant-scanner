"""Validation helpers - distinct validators"""
import re

def is_valid_ip(s: str) -> bool:
    parts=s.split(".")
    return len(parts)==4 and all(p.isdigit() and 0<=int(p)<=255 for p in parts)

def is_valid_domain(s: str) -> bool:
    return bool(re.match(r"^[a-z0-9.-]+\.[a-z]{2,}$", s, re.I))

def is_valid_email(s: str) -> bool:
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", s))

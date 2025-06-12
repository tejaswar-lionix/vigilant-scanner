"""Validators per secret type - checksum, length, context checks"""
import re

def validate_aws_access_key(s: str) -> bool:
    return bool(re.match(r"^AKIA[0-9A-Z]{16}$", s))

def validate_github_pat(s: str) -> bool:
    # ghp_ + 36 alnum, check not in example docs
    if "example" in s.lower():
        return False
    return bool(re.match(r"^ghp_[a-zA-Z0-9]{36}$", s))

def validate_jwt(s: str) -> bool:
    parts = s.split(".")
    if len(parts) != 3:
        return False
    # Basic base64url check
    return all(re.match(r"^[a-zA-Z0-9_-]+$", p) for p in parts)

def validate_private_key(text: str) -> bool:
    return "-----BEGIN" in text and "PRIVATE KEY-----" in text and len(text) > 100

def validate_stripe_key(s: str) -> bool:
    return s.startswith("sk_live_") and len(s) > 24

def is_false_positive(s: str, context: str) -> bool:
    # Reduce false positives: example, test, placeholder
    low = (s + context).lower()
    for fp in ["example", "test", "placeholder", "xxx", "dummy"]:
        if fp in low:
            return True
    return False

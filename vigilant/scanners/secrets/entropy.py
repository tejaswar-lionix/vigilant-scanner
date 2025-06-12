"""Shannon entropy for secret detection - high entropy indicates random token"""
import math
from collections import Counter

def shannon_entropy(s: str) -> float:
    if not s:
        return 0.0
    freq = Counter(s)
    length = len(s)
    entropy = -sum((count/length) * math.log2(count/length) for count in freq.values())
    return entropy

def is_high_entropy(s: str, threshold: float = 3.5) -> bool:
    # Only check strings of sufficient length and charset
    if len(s) < 20:
        return False
    # Require mixed charset for entropy signal
    has_lower = any(c.islower() for c in s)
    has_upper = any(c.isupper() for c in s)
    has_digit = any(c.isdigit() for c in s)
    if not (has_lower or has_upper):
        return False
    return shannon_entropy(s) > threshold

def entropy_for_file(content: str, window: int = 40) -> list:
    # Sliding window entropy, used to flag random blobs
    results = []
    for i in range(len(content) - window + 1):
        w = content[i:i+window]
        if is_high_entropy(w):
            results.append((i, w[:20], shannon_entropy(w)))
    return results[:10]

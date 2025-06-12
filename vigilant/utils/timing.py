"""Timing helpers - MTTR style, distinct"""
import time

def now_ms() -> int:
    return int(time.time()*1000)

def elapsed(start: float) -> float:
    return time.time() - start

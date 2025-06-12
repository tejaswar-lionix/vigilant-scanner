"""Syslog RFC5424 parser"""
import re
def parse_syslog(line: str):
    m=re.match(r"<(\d+)>(\d+)\s+(\S+)\s+(\S+)\s+(.*)", line)
    if not m:
        return None
    return {"pri":m.group(1),"host":m.group(3),"app":m.group(4),"msg":m.group(5)}

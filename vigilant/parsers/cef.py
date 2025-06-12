"""CEF parser - Common Event Format"""
import re

def parse_cef(line: str):
    # CEF:Version|Device Vendor|Device Product|Version|Signature|Name|Severity|Extension
    m=re.match(r"CEF:(\d+)\|(.*)", line)
    if not m:
        return None
    parts=line.split("|")
    if len(parts) < 7:
        return None
    return {"version":parts[0].split(":")[1],"vendor":parts[1],"product":parts[2],"severity":parts[6]}

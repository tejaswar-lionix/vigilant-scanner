"""JSON log parser"""
import json
def parse_json(line: str):
    try:
        return json.loads(line)
    except:
        return None

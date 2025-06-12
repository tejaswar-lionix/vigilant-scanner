"""JSON reporter"""
import json, pathlib

def write_json(findings, path: pathlib.Path):
    path.write_text(json.dumps({"findings":findings,"count":len(findings)}, indent=2))

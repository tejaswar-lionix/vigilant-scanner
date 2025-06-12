"""SARIF reporter - GitHub code scanning"""
import json, pathlib

def write_sarif(findings, path: pathlib.Path):
    sarif={"version":"2.1.0","runs":[{"tool":{"driver":{"name":"Vigilant"}},"results":[{"ruleId":f.get("pattern_id",""),"message":{"text":f.get("match","")},"locations":[{"physicalLocation":{"artifactLocation":{"uri":f.get("file","")}}}] } for f in findings]}]}
    path.write_text(json.dumps(sarif, indent=2))

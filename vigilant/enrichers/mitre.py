"""MITRE ATT&CK enrichment"""
MAPPING = {
    "T1071":"Command and Control: Application Layer Protocol",
    "T1059":"Execution: Command and Scripting Interpreter",
    "T1078":"Persistence: Valid Accounts",
}

def enrich_mitre(finding):
    # Map secret exfiltration to T1071
    if finding.get("platform")=="aws":
        finding["mitre"]="T1071"
        finding["tactic"]="Exfiltration"
    elif "eval" in finding.get("title",""):
        finding["mitre"]="T1059"
    return finding

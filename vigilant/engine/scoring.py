"""Scoring - CVSS-like 0-100, severity + confidence + exploitability"""
def score_finding(finding, confidence="high"):
    sev = finding.get("severity","medium")
    base = {"low":25,"medium":50,"high":75,"critical":90}.get(sev,50)
    conf_mult = {"low":0.7,"medium":0.9,"high":1.0,"confirmed":1.1}.get(confidence,1.0)
    # Adjust for platform
    if finding.get("platform") in ("aws","gcp"):
        base += 5
    return min(100, round(base*conf_mult,1))

def aggregate_score(findings):
    if not findings:
        return 0
    scores=[score_finding(f) for f in findings]
    return round(sum(scores)/len(scores),1)

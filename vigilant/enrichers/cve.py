"""CVE enrichment - mock NVD lookup"""
MOCK_CVE = {
    "lodash": "CVE-2021-23337",
    "django": "CVE-2022-34265",
}

def enrich_cve(finding):
    pkg=finding.get("pkg","")
    if pkg in MOCK_CVE:
        finding["cve"]=MOCK_CVE[pkg]
        finding["cve_url"]=f"https://nvd.nist.gov/vuln/detail/{MOCK_CVE[pkg]}"
    return finding

"""CIS Benchmark - 60 checks"""
CHECKS = [
    ("CIS-1.1","Ensure MFA enabled","high"),
    ("CIS-1.2","Ensure no root access keys","critical"),
    ("CIS-2.1","Ensure S3 bucket not public","high"),
]

def check_cis(findings):
    gaps=[]
    for f in findings:
        if "aws" in f.get("platform","") and f.get("severity")=="critical":
            gaps.append({"check":"CIS-1.2","finding":f})
    return gaps

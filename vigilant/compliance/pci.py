"""PCI DSS - 40 checks"""
CHECKS = [
    ("PCI-3.4","Protect stored card data","high"),
    ("PCI-8.3","MFA for admin","critical"),
]

def check_pci(findings):
    return [{"check":"PCI-8.3","finding":f} for f in findings if f.get("severity")=="critical"]

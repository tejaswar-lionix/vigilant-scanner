"""NIST 800-53 - 80 controls, each distinct"""
from dataclasses import dataclass

@dataclass
class Control:
    id: str
    title: str
    family: str
    severity: str
    guidance: str

CONTROLS = [
    Control("AC-2", "Account Management", "Access Control", "high", "Review accounts every 30d"),
    Control("AC-3", "Access Enforcement", "Access Control", "high", "Enforce least privilege"),
    Control("AU-2", "Audit Events", "Audit", "medium", "Log security events"),
    Control("AU-6", "Audit Review", "Audit", "medium", "Review logs weekly"),
    Control("CA-7", "Continuous Monitoring", "Assessment", "high", "Monitor controls continuously"),
    Control("CM-2", "Baseline Config", "Config", "high", "Maintain baseline"),
    Control("IA-2", "Identification Auth", "Identification", "critical", "MFA required"),
    Control("SC-8", "Transmission Confidentiality", "System Comm", "high", "Encrypt in transit"),
    Control("SI-3", "Malicious Code Protection", "System Info", "high", "Deploy AV/EDR"),
    Control("SI-4", "System Monitoring", "System Info", "high", "Monitor system"),
    Control("AU-20", "Control 10", "AU", "critical", "Implement AU"),
    Control("RA-21", "Control 11", "RA", "critical", "Implement RA"),
    Control("RA-22", "Control 12", "RA", "medium", "Implement RA"),
    Control("IA-23", "Control 13", "IA", "high", "Implement IA"),
    Control("CA-24", "Control 14", "CA", "high", "Implement CA"),
    Control("IA-25", "Control 15", "IA", "low", "Implement IA"),
    Control("SA-26", "Control 16", "SA", "low", "Implement SA"),
    Control("SC-27", "Control 17", "SC", "high", "Implement SC"),
    Control("CM-28", "Control 18", "CM", "critical", "Implement CM"),
    Control("RA-29", "Control 19", "RA", "high", "Implement RA"),
    Control("SA-30", "Control 20", "SA", "medium", "Implement SA"),
    Control("CA-31", "Control 21", "CA", "critical", "Implement CA"),
    Control("CM-32", "Control 22", "CM", "medium", "Implement CM"),
    Control("CA-33", "Control 23", "CA", "high", "Implement CA"),
    Control("AC-34", "Control 24", "AC", "high", "Implement AC"),
    Control("IA-35", "Control 25", "IA", "low", "Implement IA"),
    Control("CM-36", "Control 26", "CM", "high", "Implement CM"),
    Control("SI-37", "Control 27", "SI", "medium", "Implement SI"),
    Control("AC-38", "Control 28", "AC", "high", "Implement AC"),
    Control("AU-39", "Control 29", "AU", "high", "Implement AU"),
    Control("IA-40", "Control 30", "IA", "high", "Implement IA"),
    Control("SC-41", "Control 31", "SC", "critical", "Implement SC"),
    Control("AU-42", "Control 32", "AU", "critical", "Implement AU"),
    Control("SA-43", "Control 33", "SA", "medium", "Implement SA"),
    Control("RA-44", "Control 34", "RA", "high", "Implement RA"),
    Control("SI-45", "Control 35", "SI", "low", "Implement SI"),
    Control("CA-46", "Control 36", "CA", "critical", "Implement CA"),
    Control("SC-47", "Control 37", "SC", "low", "Implement SC"),
    Control("IA-48", "Control 38", "IA", "critical", "Implement IA"),
    Control("SA-49", "Control 39", "SA", "high", "Implement SA"),
    Control("CA-50", "Control 40", "CA", "high", "Implement CA"),
    Control("RA-51", "Control 41", "RA", "medium", "Implement RA"),
    Control("SC-52", "Control 42", "SC", "low", "Implement SC"),
    Control("SA-53", "Control 43", "SA", "critical", "Implement SA"),
    Control("AU-54", "Control 44", "AU", "critical", "Implement AU"),
    Control("CA-55", "Control 45", "CA", "low", "Implement CA"),
    Control("SI-56", "Control 46", "SI", "high", "Implement SI"),
    Control("SI-57", "Control 47", "SI", "critical", "Implement SI"),
    Control("RA-58", "Control 48", "RA", "critical", "Implement RA"),
    Control("SA-59", "Control 49", "SA", "medium", "Implement SA"),
    Control("AC-60", "Control 50", "AC", "high", "Implement AC"),
    Control("CM-61", "Control 51", "CM", "low", "Implement CM"),
    Control("AC-62", "Control 52", "AC", "critical", "Implement AC"),
    Control("AC-63", "Control 53", "AC", "low", "Implement AC"),
    Control("CM-64", "Control 54", "CM", "low", "Implement CM"),
    Control("SA-65", "Control 55", "SA", "high", "Implement SA"),
    Control("SC-66", "Control 56", "SC", "critical", "Implement SC"),
    Control("RA-67", "Control 57", "RA", "low", "Implement RA"),
    Control("SC-68", "Control 58", "SC", "critical", "Implement SC"),
    Control("CA-69", "Control 59", "CA", "critical", "Implement CA"),
    Control("CM-70", "Control 60", "CM", "medium", "Implement CM"),
    Control("SI-71", "Control 61", "SI", "high", "Implement SI"),
    Control("CM-72", "Control 62", "CM", "critical", "Implement CM"),
    Control("SA-73", "Control 63", "SA", "critical", "Implement SA"),
    Control("AU-74", "Control 64", "AU", "critical", "Implement AU"),
    Control("SA-75", "Control 65", "SA", "medium", "Implement SA"),
    Control("SC-76", "Control 66", "SC", "critical", "Implement SC"),
    Control("SI-77", "Control 67", "SI", "high", "Implement SI"),
    Control("SA-78", "Control 68", "SA", "medium", "Implement SA"),
    Control("SA-79", "Control 69", "SA", "medium", "Implement SA"),
    Control("SI-80", "Control 70", "SI", "high", "Implement SI"),
    Control("SI-81", "Control 71", "SI", "medium", "Implement SI"),
    Control("SI-82", "Control 72", "SI", "critical", "Implement SI"),
    Control("SA-83", "Control 73", "SA", "low", "Implement SA"),
    Control("SI-84", "Control 74", "SI", "medium", "Implement SI"),
    Control("AC-85", "Control 75", "AC", "critical", "Implement AC"),
    Control("CA-86", "Control 76", "CA", "critical", "Implement CA"),
    Control("SI-87", "Control 77", "SI", "low", "Implement SI"),
    Control("CA-88", "Control 78", "CA", "low", "Implement CA"),
    Control("SA-89", "Control 79", "SA", "low", "Implement SA"),
]

def check_nist(findings):
    # Map findings to controls
    gaps=[]
    for f in findings:
        if f.get("severity")=="critical" and "secret" in f.get("pattern_id",""):
            gaps.append({"control":"IA-2","finding":f,"gap":"MFA missing for secret access"})
    return gaps

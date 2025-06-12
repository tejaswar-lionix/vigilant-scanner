"""HTML reporter"""
import pathlib

def write_html(findings, path: pathlib.Path):
    html="<html><body><h1>Vigilant Report</h1><table border=1>"
    html+="<tr><th>File</th><th>Severity</th><th>Match</th></tr>"
    for f in findings:
        html+=f"<tr><td>{f.get('file','')}</td><td>{f.get('severity','')}</td><td>{f.get('match','')}</td></tr>"
    html+="</table></body></html>"
    path.write_text(html)

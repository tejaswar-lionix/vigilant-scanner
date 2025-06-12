"""CSV reporter"""
import csv, pathlib

def write_csv(findings, path: pathlib.Path):
    with open(path,"w",newline="") as f:
        w=csv.DictWriter(f, fieldnames=["file","severity","platform","match"])
        w.writeheader()
        for fi in findings:
            w.writerow({k:fi.get(k,"") for k in ["file","severity","platform","match"]})

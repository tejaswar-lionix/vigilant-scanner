import click, pathlib, json
from .scanners.secrets.scanner import scan_path

@click.group()
def cli():
    pass

@cli.command()
@click.argument("path")
@click.option("--format", "fmt", default="json", type=click.Choice(["json","sarif"]))
@click.option("--out", default="report.json")
def scan(path, fmt, out):
    findings = scan_path(pathlib.Path(path))
    pathlib.Path(out).write_text(json.dumps(findings, indent=2))
    click.echo(f"Scanned {path}: {len(findings)} findings -> {out}")

if __name__ == "__main__":
    cli()

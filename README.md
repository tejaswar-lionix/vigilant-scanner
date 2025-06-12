# Vigilant Scanner — Secret & Supply Chain Security Toolkit

Fast, offline secret detection + dependency/IaC audit + compliance posture in one binary. Designed for CI and SOC triage.

## What it does
- **Secret scanner** — 150+ patterns (AWS, GCP, GitHub, Slack, Stripe, OpenAI, JWT, private keys) + Shannon entropy (3.5+) + validators, SARIF output
- **Dependency audit** — npm/pip/Go advisory DB, transitive, fix suggestions
- **IaC scanner** — Terraform misconfigs (open S3, 0.0.0.0/0), Dockerfile (root, no pin), K8s (privileged, hostNetwork)
- **SAST lite** — 100 Python + 80 JS rules (CWE-79/89/95/78/502) via regex/AST
- **Compliance** — NIST 800-53 80 controls, CIS 60 checks, PCI 40, gap report
- **Correlation** — deduplicate findings by hash, score (CVSS-like 0-100), MITRE ATT&CK enrichment
- **Reporters** — JSON, SARIF, HTML, CSV

## Install
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
npm install
```

## Build
```bash
make build
docker build -t vigilant .
docker-compose build
npm run build
```

## Run
```bash
# CLI
python -m vigilant scan /path/to/repo --format sarif --out report.sarif
python -m vigilant scan . --entropy 3.5 --fail-high
# API
python -m vigilant.api  # -> http://localhost:8000/docs
# Frontend
npm run dev  # -> http://localhost:5173
docker-compose up
```

## Tests
```bash
pytest -q
pytest --cov=vigilant --cov-report=xml
npm test
npm run test:coverage
```

## Architecture
```
vigilant/
  scanners/secrets/ (patterns, entropy, validators, scanner)
  scanners/dependencies/ (npm, pip, go, audit)
  scanners/iac/ (terraform, dockerfile, k8s)
  scanners/sast/ (rules_python, rules_js)
  engine/ (correlation, scoring, dedupe)
  enrichers/ (mitre, cve, geoip)
  compliance/ (nist, cis, pci)
  parsers/ (cef, syslog, json, leef)
  reporters/ (json, sarif, html, csv)
frontend/src/modules/{secrets, dependencies, iac, compliance}/ (React + Vite)
```

## Dependencies
Python: FastAPI, Pydantic, Click, GitPython, PyYAML, Rich
Node: React 18, TypeScript 5, Vite 5, TanStack Query, Vitest

## License
Proprietary — All rights reserved (Vigilant Labs).

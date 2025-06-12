from vigilant.scanners.dependencies.npm import parse_package_json
from vigilant.scanners.dependencies.pip import parse_requirements
import pathlib, json, tempfile, os

def test_parse_package_json(tmp_path):
    p=tmp_path/"package.json"
    p.write_text(json.dumps({"dependencies":{"lodash":"4.17.20"}}))
    deps=parse_package_json(p)
    assert deps["lodash"]=="4.17.20"

def test_parse_requirements(tmp_path):
    p=tmp_path/"requirements.txt"
    p.write_text("Django==3.2.10\nrequests\n")
    from vigilant.scanners.dependencies.pip import parse_requirements
    deps=parse_requirements(p)
    assert deps["django"]=="3.2.10"

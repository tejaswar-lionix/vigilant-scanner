import re
from vigilant.scanners.secrets.patterns import PATTERNS

def test_aws_pattern():
    p=[x for x in PATTERNS if x.id=="aws_access_key"][0]
    assert re.match(p.regex, "AKIA_TEST_EXAMPLE")

def test_github_pat():
    p=[x for x in PATTERNS if x.id=="github_pat_old"][0]
    assert p.compiled.search("ghp_TEST_EXAMPLE_123456")

def test_entropy_filter():
    from vigilant.scanners.secrets.entropy import is_high_entropy
    assert is_high_entropy("aB3dEfGhIjKlMnOpQrStUvWxYz123456")
    assert not is_high_entropy("hello world hello world")

def test_validator():
    from vigilant.scanners.secrets.validators import validate_github_pat
    assert validate_github_pat("ghp_TEST_EXAMPLE_123456")
    assert not validate_github_pat("ghp_example")

from vigilant.compliance.nist import CONTROLS, check_nist

def test_nist_count():
    assert len(CONTROLS) >= 80

def test_nist_gap():
    findings=[{"severity":"critical","pattern_id":"aws_secret_key"}]
    gaps=check_nist(findings)
    assert any(g["control"]=="IA-2" for g in gaps)

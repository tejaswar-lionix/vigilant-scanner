from vigilant.engine.correlation import dedupe
from vigilant.engine.scoring import score_finding

def test_dedupe():
    f=[{"file":"a.py","pattern_id":"aws","line":1},{"file":"a.py","pattern_id":"aws","line":1}]
    assert len(dedupe(f))==1

def test_scoring():
    assert score_finding({"severity":"critical"}) > score_finding({"severity":"low"})

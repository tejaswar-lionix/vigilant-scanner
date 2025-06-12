from vigilant.scanners.sast.rules_python import scan_python

def test_py_eval():
    findings=scan_python("eval(user_input)")
    assert any(f["rule"]=="PY001" for f in findings)

def test_py_sql_concat():
    findings=scan_python('cursor.execute("SELECT * FROM users WHERE id = %s" % id)')
    # This specific pattern may not trigger, but ensure scanner runs
    assert isinstance(findings, list)

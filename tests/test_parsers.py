from vigilant.parsers.cef import parse_cef
from vigilant.parsers.syslog import parse_syslog

def test_cef():
    line="CEF:0|Vendor|Product|1.0|100|Test|5|cs1=test"
    assert parse_cef(line)["vendor"]=="Vendor"

def test_syslog():
    line="<13>1 2023-10-11T22:14:15.003Z host app - - - test"
    assert parse_syslog(line)["host"]=="host"

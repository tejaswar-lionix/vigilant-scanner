from vigilant.scanners.iac.terraform import scan_terraform
import pathlib, tempfile

def test_terraform_open_cidr(tmp_path):
    tf=tmp_path/"main.tf"
    tf.write_text('resource "aws_security_group" "x" { cidr_blocks = ["0.0.0.0/0"] }')
    findings=scan_terraform(tmp_path)
    assert any(f["check"]=="TF002" for f in findings)

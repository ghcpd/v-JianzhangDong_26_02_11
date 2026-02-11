import subprocess
import sys

def test_ci_script_fails():
    result = subprocess.run(
        [sys.executable, "ci_pipeline.py"],
        capture_output=True,
        text=True
    )
    assert "CI FAILED" in result.stdout

import subprocess
import sys
import os

def run_tests():
    print("=== Running CI Pipeline ===")

    # 模拟 CI 忘记设置环境变量
    if "DATA_PATH" in os.environ:
        del os.environ["DATA_PATH"]

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests"],
        capture_output=True,
        text=True
    )

    print(result.stdout)
    print(result.stderr)

    if result.returncode != 0:
        print("CI FAILED")
        sys.exit(1)

    print("CI PASSED")

if __name__ == "__main__":
    run_tests()

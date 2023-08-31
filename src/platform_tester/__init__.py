import platform
import subprocess
import sys


def main():
    print(f"System: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Platform: {platform.platform()}")
    # if sys.platform == "darwin":
    #     print("osx")
    # if sys.platform == "win32":
    #     print("windows")
    # if sys.platform == "linux":
    #     tmp = subprocess.check_output(["grep", "-i", "Microsoft", "/proc/version"])
    #     print(tmp.stdout)
    #     if subprocess.run(["grep", "-i", "Microsoft", "/proc/version"]):
    #         print("Linux WSL")
    #     else:
    #         print("linux")
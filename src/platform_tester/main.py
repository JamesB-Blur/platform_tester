import platform
import subprocess
import sys


def main():
    print(f"System: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Platform: {platform.platform()}")
    # if sys.platform == "darwin":

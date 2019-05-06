#!/usr/bin/env python3

import os
import subprocess

if __name__ == "__main__":
    os.symlink("build/compile_commands.json", "compile_commands.json")
    subprocess.run(["cmake", "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON", ".."], cwd="build")
    subprocess.run(["git", "init"])

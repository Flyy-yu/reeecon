# All utility functions

import subprocess


def run_tool(tool_name, args):
    res = subprocess.run([tool_name, args])
    if res.returncode == 0:
        return True
    else:
        return False

# All utility functions

import subprocess

def run_tool(args):
    args_arr = args.split(' ')
    res = subprocess.run(args_arr)
    if res.returncode == 0:
        return True
    else:
        return False


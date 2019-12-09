# All utility functions

import subprocess


def run_tool(args):
    args_arr = args.split(' ')
    res = subprocess.run(args_arr)
    if res.returncode == 0:
        return True
    else:
        return False


def get_directory_filename(url):
    if 'https' in url:
        filename = url.replace('https://', '') + '_https'
    else:
        filename = url.replace('http://', '') + '_http'
    return filename

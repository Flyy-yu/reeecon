# All utility functions

import subprocess


def run_tool(args):
    #TODO disable Stdout?
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


def convert_to_html(path):
    with open(path + 'responsive.txt', 'r') as f:
        with open(path + 'responsive.html', 'w') as fw:
            line = f.readline().replace('\n', '')
            while line:
                html_line = '<a href="{}">{}</a><br>'.format(line, line)
                fw.writelines(html_line)
                line = f.readline().replace('\n', '')

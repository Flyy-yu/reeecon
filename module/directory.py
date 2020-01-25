from .util import *

dirs_path = '/root/dirsearch/dirsearch.py'
f_ext = 'php,asp,aspx,jsp,html,zip'


def use_dirsearch_full_url(url, wordlist, out_dir):
    filename = get_directory_filename(url) + '_dirsearch.txt'
    out_dir = out_dir + filename
    run_tool('python3 {} -u {} -b -w {} -t 50 -E --plain-text-report {}'
             .format(dirs_path, url, wordlist, out_dir))
    return


def use_dirsearch_short_url(url, wordlist, out_dir):
    filename = get_directory_filename(url) + '_dirsearch.txt'
    out_dir = out_dir + filename
    run_tool('python3 {} -u {} -b -w {} -t 50 -e {} --plain-text-report {}'
             .format(dirs_path, url, wordlist, f_ext, out_dir))
    return


def use_gobuster(url, wordlist, out_dir):
    filename = get_directory_filename(url) + '_gobuster.txt'
    out_dir = out_dir + filename
    run_tool('gobuster dir -u {} -w {} -o {} -t 20 --wildcard'
             .format(url, wordlist, out_dir))
    return

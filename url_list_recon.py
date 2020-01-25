import os
import sys
import json
import pathlib
from module.subdomain import *
from module.directory import *
from datetime import date

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

today = date.today().strftime("%b-%d-%Y")

if __name__ == '__main__':

    try:
        target = sys.argv[1]
    except IndexError:
        exit('Usage: python3 url_list_recon.py $target.txt')

    # TODO better path
    out_dir = '/root/recon_result/{}/{}/'.format(target, today)

    run_tool('mkdir -p ' + out_dir)
    run_tool('cp {} {}'.format(target, out_dir + 'responsive.txt'))

    # directory brute force with gobuster
    print("****directory brute force****")

    directory_path = out_dir + 'directory/'

    try:
        pathlib.Path(directory_path).mkdir(parents=True)
    except FileExistsError:
        print('directory already exists')
        pass

    with open('{}responsive.txt'.format(out_dir), 'r') as f:
        line = f.readline().replace('\n', '').replace('\r', '')
        while line:
            use_dirsearch_short_url(line, config['top1000'], directory_path)
            use_gobuster(line, config['top1000'], directory_path)
            line = f.readline().replace('\n', '').replace('\r', '')

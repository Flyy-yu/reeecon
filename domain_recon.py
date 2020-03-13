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
        exit('Usage: python3 domain_recon.py $target(domain)')

    # TODO better path
    out_dir = '/root/recon_result/{}/{}/'.format(target, today)

    # subdomain recon with amass and subfinder
    print("****subdomain recon****")
    subdomain_path = out_dir + 'subdomain/'

    try:
        pathlib.Path(subdomain_path).mkdir(parents=True)
        use_amass(target, subdomain_path)
        use_subfinder(target, subdomain_path)

        os.system('cat {}* | sort --unique > {}subdomain.txt'.format(subdomain_path,
                                                                     out_dir))

        os.system('cat {}subdomain.txt | httprobe -c 50 -t 3000 > {}responsive.txt'
                  .format(out_dir, out_dir))
    except FileExistsError:
        print("directory already exists")
        pass

    smuggling_path = out_dir + "smuggling.txt"
    os.system('python3 module/Smuggling_download.py -u {}responsive.txt -of {}'.format(out_dir, smuggling_path))

    convert_to_html(out_dir)
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
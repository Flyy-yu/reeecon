import sys
import json
import pathlib
import argparse
from module.subdomain import *
from module.directory import *
from module.subdomain_takeover import *
from module.screenshot import *
from datetime import date

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

today = date.today().strftime("%b-%d-%Y")

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", help="Github auth token for github_subdomain.py")
    parser.add_argument("-d", "--domain", help="The target domain", required=True)
    parser.parse_args()
    args = parser.parse_args()

    target = args.domain

    # TODO better path
    out_dir = '{}/recon_result/{}/{}/'.format(home, target, today)

    os.system('rm -r {}'.format(out_dir))

    print("****subdomain recon****")
    subdomain_path = out_dir + 'subdomain/'

    try:
        pathlib.Path(subdomain_path).mkdir(parents=True)
        use_amass(target, subdomain_path)
        use_subfinder(target, subdomain_path)
        use_sublist3r(target, subdomain_path)

        if args.token:
            use_github_subdomains(target, subdomain_path, args.token)

        os.system('cat {}* | sort --unique > {}subdomain.txt'.format(subdomain_path,
                                                                     out_dir))

        # Check for sub-domain takeover
        print("****Checking for potential subdomain takeover, this will take a while****")
        subdomain_takeover(out_dir, target)
        os.system('cat {}subdomain.txt | httprobe -c 50 -t 3000 > {}responsive.txt'
                  .format(out_dir, out_dir))
    except FileExistsError:
        print("Directory found")
        pass

    # Remove the ending "." in responsive.txt
    remove_ending_dot(out_dir)

    # convert responsive.txt to responsive.html
    convert_to_html(out_dir)

    # screenshot with AQUATONE
    print("****Getting screenshot with AQUATONE, it take a while****")
    use_aquatone(out_dir)

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

    # Check for request smuggling
    smuggling_path = out_dir + "smuggling.txt"
    os.system('python3 module/Smuggling_download.py -u {}responsive.txt -of {}'.format(out_dir, smuggling_path))

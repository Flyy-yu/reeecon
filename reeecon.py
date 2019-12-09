import pathlib
import os
from module.subdomain import *
from datetime import date

today = date.today().strftime("%b-%d-%Y")

if __name__ == '__main__':
    target = 'certik'

    # TODO better path
    out_dir = '/root/recon_result/{}/{}/'.format(target, today)

    print("subdomain recon:")
    subdomain_path = out_dir + 'subdomain/'
    pathlib.Path(subdomain_path).mkdir(parents=True)

    use_amass('certik.org', subdomain_path)
    use_subfinder('certik.org', subdomain_path)

    os.system('cat {}* | sort --unique > {}subdomain.txt'.format(subdomain_path, out_dir))
    os.system('cat {}subdomain.txt | httprobe -c 50 -t 3000 > {}responsive.txt'.format(out_dir, out_dir))

    
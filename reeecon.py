import pathlib
from .module.subdomain import *
from datetime import date

today = date.today().strftime("%b-%d-%Y")

if __name__ == '__main__':
    target = 'certik'

    # TODO better path
    out_dir = '/root/recon_result/{}/{}/'.format(today, target)

    print("subdomain recon:")
    subdomain_path = out_dir + 'subdomain/'
    pathlib.Path(subdomain_path).mkdir(parents=True, exist_ok=True)

    use_amass('certik.org', subdomain_path)
    use_subfinder('certik.org', subdomain_path)

    run_tool('cat {} | --sort --unique > ../subdomain.txt'.format(subdomain_path))

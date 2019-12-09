import pathlib
from module.subdomain import *
from datetime import date

today = date.today().strftime("%b-%d-%Y")

if __name__ == '__main__':
    target = 'certik'

    out_dir = '~/recon_result/{}/{}/'.format(today, target)

    pathlib.Path(out_dir + 'subdomain').mkdir(parents=True, exist_ok=True)

    use_amass('certik.org', out_dir)

    use_subfinder('certik.org', out_dir)

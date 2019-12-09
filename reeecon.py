from module.subdomain import *

if __name__ == '__main__':
    target = 'certik'

    out_dir = '~/recon_result/' + target + '/'

    use_amass('certik.org', out_dir)

    use_subfinder('certik.org', out_dir)

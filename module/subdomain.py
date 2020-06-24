# module for subdomain enumeration

from .util import *
from datetime import date

today = date.today().strftime("%b-%d-%Y")
massdnsWordlist = home + "/wordlist/dns-Jhaddix.txt"

def use_amass(domain, out_dir):
    run_tool('amass enum -d {} -o {}'.format(domain, out_dir + 'amass.txt'))
    pass


def use_subfinder(domain, out_dir):
    run_tool('subfinder -d {} -o {}'.format(domain, out_dir + 'subfinder.txt'))
    pass


def use_sublist3r(domain, out_dir):
    run_tool('python3 {}/tools/Sublist3r/sublist3r.py -d {} -t 10 -o {}'.format(home, domain, out_dir + 'sublist3r.txt'))
    pass
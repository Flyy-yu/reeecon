# module for subdomain enumeration

from .util import *


def use_amass(domain, out_dir):
    run_tool('amass enum -d {} -o {}'.format(domain, out_dir + 'amass.txt'))
    pass


def use_subfinder(domain, out_dir):
    run_tool('subfinder -d {} -o {}'.format(domain, out_dir + 'subfinder.txt'))
    pass

import os
from .util import *


def use_aquatone(out_dir):
    responsive_url_list = out_dir + 'responsive.txt'

    os.system('cat {} | aquatone -chrome-path {}/chromium-latest-linux/latest/chrome -out {} -threads 5 -silent'
              .format(responsive_url_list, home, out_dir))
    return

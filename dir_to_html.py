import os
import sys
import json
import pathlib
from module.subdomain import *
from module.directory import *
from datetime import date

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

if __name__ == '__main__':
    convert_to_html("")

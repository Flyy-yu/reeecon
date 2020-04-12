#!/usr/bin/env python3
import sys
import urllib.request
import urllib.parse
import re
import os
from datetime import date

today = date.today().strftime("%b-%d-%Y")
massdnsWordlist = "/root/wordlist/dns-Jhaddix.txt"


def subdomain_takeover(out_dir, target):
    domains = set()
    for i, arg in enumerate(sys.argv, 1):
        with urllib.request.urlopen('https://crt.sh/?q=' + urllib.parse.quote('%.' + arg)) as f:
            code = f.read().decode('utf-8')
            for cert, domain in re.findall(
                    '<tr>(?:\s|\S)?href="\?id=([0-9]+?)"(?:\s|\S)?<td>([_a-zA-Z0-9.-]+?\.' + re.escape(
                        arg) + ')</td>(?:\s|\S)?</tr>', code, re.IGNORECASE):
                domain = domain.split('@')[-1]
                if not domain in domains:
                    domains.add(domain)
                    print(domain)

    with open(out_dir + "domaintemp.txt", "a") as text_file:
        for item in domains:
            text_file.write("%s\n" % item)

    os.system(
        'cat {} | /root/tools/massdns/bin/massdns -r /root/tools/massdns/lists/resolvers.txt -t A -q -o S -w {}domaintemp.txt'.format(
            out_dir + 'subdomain.txt', out_dir))
    os.system(
        '/root/tools/massdns/scripts/subbrute.py {} {} | /root/tools/massdns/bin/massdns -r /root/tools/massdns/lists/resolvers.txt -t A -q -o S | grep -v 142.54.173.92 >> {}domaintemp.txt'.format(
            massdnsWordlist, target, out_dir))
    test_subdomain = {}
    with open(out_dir + "domaintemp.txt", "r") as text_file:
        lines = text_file.readlines()
        for line in lines:
            record = line.split(' ')
            if record[1] == "CNAME" and record[2] not in test_subdomain.values():
                test_subdomain[record[0]] = record[2]

    with open(out_dir + "subdomain_takeover.txt", "a") as f:
        f.writelines('check the following domains for NS takeover:')
        for subdomain in test_subdomain.keys():
            output = os.popen("host {}".format(subdomain)).read()
            if "NXDOMAIN" in output:
                f.writelines(subdomain + '\n')

# subdomain_takeover('/root/recon_result/marriott.com/Mar-15-2020/', 'marriott.com')

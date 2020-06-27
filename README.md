# reeecon

Bug bounty domain recon.
<br>
Inspired by https://github.com/nahamsec/lazyrecon. Rewrite it in python. 

# Install
1. Downlaod and run the setup script: 
https://github.com/Flyy-yu/public_script/blob/master/vps_setup.sh

2. `source ~/.bashrc`

3. Enjoy

# Usage

`python3 domain_recon.py -d example.com`

```
usage: domain_recon.py [-h] [-t TOKEN] -d DOMAIN

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Github auth token for github_subdomain.py
  -d DOMAIN, --domain DOMAIN
                        The target domain
```

# What's included?

- Subdomain recon: amass + subfinder + sublist3r + github-subdomains.py 
- Check responsive hosts: httprobe
- Directory brute force: gobuster + dirsearch
- Screenshot: Aquatone 
- Subdomain takeover: massdns
- Request smuggling(kind of useless...): https://github.com/gwen001/pentest-tools/blob/master/smuggler.py

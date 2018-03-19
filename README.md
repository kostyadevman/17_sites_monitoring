# Sites Monitoring Utility

The script check URLs given in the text file for response the status code and an expiration date. In case of response code is 200 and expiration time more than a month script print "True"
in other case - "False"

The script requires the installed Python interpreter version 3.5
```bash 
$ pip install -r requirements.txt
``` 
File content:
```bash
https://www.google.ru
https://devman.org
https://github.com
```

# Exampele of on Linux, Python 3.5:


```bash
$ python check_sites_health.py <path to file>
Site https://www.google.ru is ok: True
Domain www.google.ru expiration time more than 30 days: True
  
Site https://devman.org is ok: True
Domain devman.org expiration time more than 30 days: True
  
Site https://github.com is ok: True
Domain github.com expiration time more than 30 days: True
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

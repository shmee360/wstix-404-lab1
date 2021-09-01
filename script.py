#!/usr/bin/env python

import requests

# print('Module Version:', requests.__version__, end='\n\n')

# r = requests.get('http://www.google.com/')
r = requests.get('https://raw.githubusercontent.com/shmee360/wstix-404-lab1/master/script.py')

# print('Status Code:', r.status_code, end='\n\n')
# print('Full Text:', r.text, sep='\n')

print(r.text)

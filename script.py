#!/usr/bin/env python

import requests

print('Module Version:', requests.__version__, end='\n\n')

r = requests.get('http://www.google.com/')

print('Status Code:', r.status_code, end='\n\n')
print('Full Text:', r.text, sep='\n')

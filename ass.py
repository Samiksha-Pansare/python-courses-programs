# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
c=0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    c=c+1
    if c!=3:
        continue
    else:
        print(tag.get('href', None))
        link=tag.get('href', None)
        print(link)
html5 = urllib.request.urlopen(link, context=ctx).read()
soup5 = BeautifulSoup(html5, 'html.parser')

# Retrieve all of the anchor tags
tags5 = soup5('a')
for tag in tags5:
    c=c+1
    if c!=3:
        continue
    else:
        print(tag.get('href', None))

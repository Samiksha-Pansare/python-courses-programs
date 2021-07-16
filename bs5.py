# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count=input("Enter the count:")
count=float(count)
position=input("Enter the position:")
position=int(position)
n=position-1
# Retrieve all of the anchor tags
tags = soup('a')


while count > 0:
    tag = tags[n]
    print(count)
    count = count-1
    print('Contents',tag.contents[0])
    u=tag.get('href', None)
    print(tag.get('href', None))
    html = urllib.request.urlopen(u, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a') 


	
	
	
	  
	
	
	
	        
    	    
    	     

    		
    	
    		
    		
    		
    		
    		
import urllib.request,urllib.parse,urllib.error
import json
sum=0
while True:
    url=input('Enter location service:')
    if len(url) < 1 : break
    print('Retrieving',url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print('Retrieved',len(data),'characters')

    info = json.loads(data)
    print('User count:', len(info))
    for line in info:
        i=0
        c=info["comments"][i]["count"] 
        print(c) 
        i=i+1
        sum=sum+c
        print(sum)    
    

import json
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
data=data.decode()

info = json.loads(data)
sum=0
comments=info["comments"]
print('Count :',len(comments))
for comment in comments:
    sum=sum+comment["count"]

print("Sum :",sum)

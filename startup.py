#!/usr/bin/python
from subprocess import call
from os import popen
from time import sleep
import requests, hmac, json, hashlib, time

path = "/home/pi/dealguy/"

# Launch ngrok
popen(path +"ngrok http 3000 &")

sleep(5)

# Call ngrok api to get url
request = requests.get('http://localhost:4040/api/tunnels')
url = json.loads(request.text)["tunnels"][0]["public_url"]

print "ngrok url is: " + url

token = '[REDACTED]'
request = requests.post('https://REDACTED.com/deals/set-domain', data={'url': url, 'token': token})
print request.text

print call(["node", path + "index.js"])

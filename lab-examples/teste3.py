import urllib3

http = urllib3.PoolManager()

r = http.request('GET', 'https://api.thingspeak.com/channels/1079343/fields/1.json?api_key=YRCLNNNCGHGP6LR8&results=2')

print(r.data)

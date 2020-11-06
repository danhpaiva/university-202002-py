import urllib3

http = urllib3.PoolManager()

r = http.request('GET', 'https://api.thingspeak.com/update?api_key=92LAK7VNBEYKDKME&field1=12')

print(r.data)
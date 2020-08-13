import requests
import json
url = 'http://10.130.113.27/api/988112a4e198cc1211/lights/4/state'


data = "{\r\n  \"on\": true,\r\n  \"bri\": 200,\r\n \"hue\": 43680,\r\n , \r\n \"sat\": 255,\r\n \"transitiontime\": 10  \r\n}\r\n"
headers ={ "Content-Type":"text/plain"}

response = requests.put(url, headers=headers,data=data)
print(response.text.encode('utf8'))

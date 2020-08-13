import requests

url = "http://10.130.113.27/api/988112a4e198cc1211/lights/2"

data = "{\r\n  \"on\": true,\r\n " \
       " \"bri\": 100,\r\n  \r\n}\r\n"
headers = {
  'Content-Type': 'text/plain'
}

response = requests.delete( url, headers=headers, data = data)

print(response.text.encode('utf8'))
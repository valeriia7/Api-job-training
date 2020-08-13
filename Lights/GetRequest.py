import requests
import json

url = "http://10.130.113.27/api/988112a4e198cc1211/lights"

res = requests.get(url)

# Parse response to json
getLights = json.loads(res.text.encode('utf8'))
print(getLights)


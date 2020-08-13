import requests

url = "http://10.130.113.27/api/988112a4e198cc1211/sensors"

# Create Sensor
body = "{\r\n\"config\": {\r\n\"on\": true\r\n\"reachable\": true\r\n}" \
          "\r\n\"manufacturername\": \"Me\"" \
          "\r\n\"modelid\": \"T1000\"" \
          "\r\n\"name\": \"My Switch\"" \
          "\r\n \"swversion\": \"1.0\"" \
          "\r\n\"type\": \"CLIPSwitch\"" \
          "\r\n \"uniqueid\": \"0x00212effff00a6b1\"\r\n}\r\n"
headers = {
  'Content-Type': 'text/plain'
}

response = requests.post(url, headers=headers, data = body)

print(response.text.encode('utf8'))

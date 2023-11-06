import socket
import requests
import pprint
import json

input_url = input("Enter Domain or URL: ")

# Memeriksa apakah URL dimulai dengan "http://" atau "https://"
if not input_url.startswith("http://") and not input_url.startswith("https://"):
    input_url = "http://" + input_url

# Mendapatkan alamat IP dari URL
hostname = input_url.split('//')[1]
ip_address = socket.gethostbyname(hostname)

request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)

geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)

for key, value in geolocation.items():
    print(str(key) + " : " + str(value))

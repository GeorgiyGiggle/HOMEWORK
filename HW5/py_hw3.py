import requests

api_backend = "http://ip-api.com/json/54.34.12.10"

req = requests.get(api_backend)

print(req.json())

data = req.json()

print(data.get("city"))
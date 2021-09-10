# 192.168.0.89
import requests

URL = requests.get("https://ipinfo.io/")
data = URL.json()

print(data['city'])
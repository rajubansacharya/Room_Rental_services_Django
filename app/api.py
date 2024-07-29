import json
import requests


x = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={a500671176cfa8391d6cd9101e6d796d}')
data = x.json()
print(data)
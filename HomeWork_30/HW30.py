import requests
import random
from pprint import pprint


sites = ['google.com', 'facebook.com', 'twitter.com', 'amazon.com', 'apple.com']

random_site = random.choice(sites)
response = requests.get('http://' + random_site)
print('Site:', random_site)
print('Status code:', response.status_code)
print('HTML length:', len(response.text))

#-----------------------------------------------------

API_key = '9adde29e77fb66f332276056c1a28332'


from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Tester")
adress = str(input('Введите адрес: \n'))
location = geolocator.geocode(adress)
print(location)
lat = location.latitude
lon = location.longitude

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={'9adde29e77fb66f332276056c1a28332'}&units=metric")
pprint(response.content)

data = response.json()
pprint(data)
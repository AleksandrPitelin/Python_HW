import requests
import random


sites = ['google.com', 'facebook.com', 'twitter.com', 'amazon.com', 'apple.com']


random_site = random.choice(sites)


response = requests.get('http://' + random_site)


print('Site:', random_site)
print('Status code:', response.status_code)
print('HTML length:', len(response.text))



while True:
    def get_city_coordinates(city_name):
        url = f'https://geocoding-api.open-meteo.com/v1/search?name={city_name}'
        response = requests.get(url)
        data = response.json()
        if 'features' in data and data['features']:
            longitude, latitude = data['features'][0]['geometry']['coordinates']
            return longitude, latitude
        return None



    def get_weather_data(longitude, latitude):
        super.__init__(longitude,latitude)
        url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}'
        response = requests.get(url)
        data = response.json()
        if 'current_weather' in data:
            return data['current_weather']
        return None

    city_name = input('Введіть назву міста: ')

    coordinates = get_city_coordinates(city_name)
    if coordinates is None:
        print(f'Не вдалося знайти координати для міста "{city_name}"')
    else:
        longitude, latitude = coordinates
        weather_data = get_weather_data(longitude, latitude)
        if weather_data is None:
            print(f'Не вдалося отримати показники погоди для міста "{city_name}"')
        else:
            print(f'Поточна погода в місті "{city_name}":')
            print(f'Температура: {weather_data["temperature"]}°C')
            print(f'Вологість: {weather_data["humidity"]}%')
            print(f'Тиск: {weather_data["pressure"]} мм рт. ст.')
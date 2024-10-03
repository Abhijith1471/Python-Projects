# Weather Application Using API
import requests

API_KEY = 'ebe810dba45b8852d8dd2710e31c8139'
BASE_URL = 'https://api.openweathermap.org/data/2.5/'

def get_weather(city):
    response = requests.get(f'{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric')
    data = response.json()
    if data.get('cod') == 200:
        weather = data['main']
        print(f"Current Temperature in {city}: {weather['temp']}°C")
    else:
        print(f"Error: {data['message']}")

def get_forecast(city):
    response = requests.get(f'{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric')
    data = response.json()
    if data.get('cod') == "200":
        for forecast in data['list'][:5]:
            print(forecast['dt_txt'], forecast['main']['temp'])
    else:
        print(f"Error: {data['message']}")

city = input("Enter the city: ")
get_weather(city)
get_forecast(city)

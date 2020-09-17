# 2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
import json
import requests

host = "https://api.weatherbit.io"
url = f"{host}/v2.0"
api_key = "d970afdd09d347e2865682a3810b7900"
timeout_s = 7


def get_current_weather_city(city):
    response = requests.get(f"{url}/current?city={city}&key={api_key}", timeout=timeout_s)
    with open("weather_city.json", "w") as file:
        json.dump(response.json(), file, indent=2)


get_current_weather_city("Moscow") 

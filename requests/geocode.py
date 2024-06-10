import requests
import time
from pprint import pprint

url = "https://geocode.maps.co/reverse"
token = ""

def find_uk_city(coordinates:list) -> str:
    uk_cities = ["Leeds", "London", "Liverpool", "Manchester", "Oxford", "Edinburgh", "Norwich", "York"]
    result_list = []
    for latitude,longitude in coordinates:
        params = {"lat": latitude, "lon": longitude, "api_key": token}
        response = requests.get(url, params=params).json()
        time.sleep(2)
        if response["address"]["city"] in uk_cities:
            result_list.append(response["address"]["city"])
    return result_list

result = find_uk_city([('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')])

print(result)
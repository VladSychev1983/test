import requests


def get_swapi_people():

    next_link = "https://swapi.py4e.com/api/people"

    while next_link:
        response = requests.get(next_link).json()
        next_link = response["next"]
        results = response["results"]
        for item in results:
            yield item


swapi_people_tall = (
    item
    for item in get_swapi_people()
    if item["height"] not in {"unknown", "none"} and int(item["height"]) > 180
)

for item in swapi_people_tall:
    print(item)

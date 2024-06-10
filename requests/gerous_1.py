"""
написать функцию самого умного супергероя среди Hulk, Captain America, Thanos.
"""
import requests
from pprint import pprint

def get_the_smartest_superhero() -> str:
    superhero_list = ["Hulk", "Captain America", "Thanos"]
    superhero_dict = {}
    the_smartest_superhero = ""
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    resonse = requests.get(url)

    #with open("all.json","wt") as f:
    #    f.write(resonse.text)

    resonse_list = resonse.json()   #список словарей.

    for list_ in resonse_list:
        if list_["name"] in superhero_list:
            print(list_["id"], list_["name"],list_["powerstats"]["intelligence"])
            superhero_dict[list_["name"]] = list_["powerstats"]["intelligence"]
    superhero_dict_sorted = dict(sorted([(k,v) for k, v in superhero_dict.items()],reverse=True, key=lambda x: x[1])[:1])
    the_smartest_superhero = list(superhero_dict_sorted.keys())[0]
    #print(list(superhero_dict_sorted.keys())[0])

    # ваш код здесь
    return the_smartest_superhero

get_the_smartest_superhero()

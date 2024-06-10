import requests
from pprint import pprint

token = ""
url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'

def translate_word(word):
    params = { "key": token, "lang": "ru-en", "text" : word}
    trans_word = ''
    response = requests.get(url, params=params)
    res_dict = response.json()
    trans_word = res_dict["def"][0]["tr"][0]["text"]
    print(res_dict["def"][0]["tr"][0]["text"])
    #return trans_word

def translate_word_en(word):
    params = { "key": token, "lang": "en-ru", "text" : word}
    trans_word = ''
    response = requests.get(url, params=params)
    res_dict = response.json()
    trans_word = res_dict["def"][0]["tr"][0]["text"]
    print(res_dict["def"][0]["tr"][0]["text"])
    
# translate_word('пиво')
# translate_word('мир')
# translate_word('еда')
translate_word_en('Birdseed')

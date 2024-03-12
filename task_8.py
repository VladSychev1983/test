import json
import xml.etree.ElementTree as ET
from pprint import pprint

parse_files = ["newsafr.json","newsafr.xml"]

def top_10(words_list,file):
    result_dict = {}
    counter = 0
    for word in words_list:
        if word in words_list and len(word) > 6 and word.isnumeric() == False:
            counter += 1
            result_dict[word] = counter
        else:
            result_dict[word] = 1     
    result_dict_sorted = dict(sorted([(k,v) for k, v in result_dict.items()],reverse=True, key=lambda x: x[1])[:10])
    print(f'Топ-10 встречающихся слов в {file}:')
    for word,quantity in result_dict_sorted.items():
        print(f'{word} - {quantity} раз')

def parse_json():
    words_list = []
    with open(parse_files[0],"rt", encoding="utf-8") as f:
        json_data = json.load(f)
        news_list = json_data["rss"]["channel"]["items"]
        for x in news_list:
            words_list.append(x["title"].split(" "))
            words_list.append(x["description"].split(" "))
        words_list = sum(words_list,[])
    top_10(words_list,parse_files[0])

print(f'===Task1===')
parse_json()

def parse_xml():
    words_list = []
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(parse_files[1], parser)
    root = tree.getroot()
    news_list = root.findall("channel/item")
    for row in news_list:
        title = row.find("title")
        description = row.find("description")
        words_list.append(title.text.split(" "))
        words_list.append(description.text.split(" "))
    words_list = sum(words_list,[])
    top_10(words_list,parse_files[1])

print(f'===Task2===')
parse_xml()
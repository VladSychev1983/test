"""
словарь - неупорядоченный обькт с доспупом по ключу.
{key:value1,key:value2}
доступ к значением словаря по ключу.
ключи в словаре уникальные.
ключами могут быть неизменяемые типы данных : числа, строки, кортежи.
значениями могут быть любые типы данных.
Общие операции
len(), copy(), deepcopy(), clear()
работа с ключами.
keys(), values (), items()
добавление /удаление элементов , объединение словарей.
del , pop(), get(), setdefault(), update()
"""
#пустой словарь.
contries_dict = dict()
contries_dict = {}

contries_dict = {"Россия":"Москва","Белоруссия":"Минск", "Франция":"Париж"}

#создать словарь из списка.
new_dict = dict.fromkeys(["Россия","Белоруссия","Франция"],"")

#print(new_dict)
print(contries_dict["Россия"])

#вывести ключе если он присутствует в словаре.
if "Турция" in contries_dict.keys():
    print(contries_dict["Турция"])
else:
    print("None")
    
print(contries_dict.get("Турция"))

#вывод ключей циклом for.
for k in contries_dict.keys():
    print(k)

for k in contries_dict:
    print(k)

print(contries_dict.keys())
print(contries_dict.values())

#ключи превратить в список.
keys_list = list(contries_dict.keys())
values_list = list(contries_dict.values())
print(keys_list)
print(keys_list)

#вернуть ключи и значене.
items_list = list(contries_dict.items())
print(items_list)
# обраться к двум значениям одновременно.
for k in contries_dict:
    print(k, contries_dict[k])

#перебор значений словаря и формирование нужного списка с последующим преобразованием списка в строку через join.
pair_list = []
for k,v in contries_dict.items():
    print(k,v)
    pair = k + " " + v
    pair_list.append(pair)
print(pair_list)
print("; ".join(pair_list))

#добавление элемента.
contries_dict["Турция"] = "Анкара"
print(contries_dict)

#удаление элемента del
del contries_dict["Турция"]
print(contries_dict)

#удаление элемента pop
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
key_to_delete = 'model'
value = car.pop("model")
print(key_to_delete, value)
print(car)

#объединение словарей.
dict1 = {"1":"one", "2":"two", "3":"three"}
dict2 = {"4":"four","5":"five","6":"six"}
dict1.update(dict2)
print(dict1)

#добавление элемента через setdefault , setdefault проверяет ключи и если ключ уже существует ничего не добавляет.
dict1.setdefault("1","one")
print(dict1)

#создать словарь где списки являются ключами.
new_key_list = ["Россия", "Беларусь", "Франция"]
countries_dict4 = {}
for key in keys_list:
    countries_dict4.setdefault(key,[])
    countries_dict4[key].append("Первый город")        
countries_dict4["Франция"].append("Париж")
print(countries_dict4)

#пример где ключем является кортеж. коды номеров телефонов: город.  Поиск ключа по значению.
countries_dict = {
    "Россия":["Москва","Санкт-Петербург","Клин"],
    "Белоруссия":["Минск","Гомель","Ровель"],
    "Германия":["Берлин","Дюссельдорф","Мюнхен"],
    "Франция":["Париж","Страсбург"]
}
phonescodes_dict = {
    (7, 3012):"Улан-Удэ",
    (7, 495):"Москва",
    (7, 499):"Москва",
    (7, 812):"Санкт-Петербург",
    (49, 211): "Дюссельдорф"
}
code = (49, 211)
city = phonescodes_dict[code]
print(phonescodes_dict[code])

for country,cites in countries_dict.items():
    if city in cites:
        print(country)
    #print(country,cites)
    
from pprint import pprint
pprint(phonescodes_dict)

#enumerate() учитывает индекс при переборе в цикле for. Завать необходимо индекс, значение.


    

    






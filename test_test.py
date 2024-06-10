
list_one = [[1,2,3,4],[5,6,7,9,10]]
list_two = ['one','two','three','four','five','six','seven','eight','night','ten']
dict_= {}

counter_iter = 0
new_list = []
for index,num in enumerate(list_one):
    counter_iter += 1
    if index == 0:
        list = []
        for n in num:
            list.append(n)
            new_list += [list]
    elif index == 1:
        list = []
        for n in num:
            list.append(n)
            new_list += [list]
print(new_list)

num = 4
print(range(num) == [0,1,2,3])

for num in range(len(list_two)):
    print(num)
    

test_list = []
test_list.append({1,3,4})
test_list.append({"id":"jf9u293uu99jfj33","message": "error" })

dic_keys = test_list[1].values()
print(dic_keys)
my_val = test_list[1].get("id")
print(my_val)

for key,value in test_list[1].items():
    print(key,value)

print(type(test_list[1]))
print(test_list)

#создать словарь из списка и значений.
d = dict.fromkeys(['Вася'], 0)
d = dict.fromkeys(['Петя'], 0)
print(d)

#тернарный метод написания условных операторов.
age = 20
print('Вы совершеннолетний!') if age >= 18 else print("Вы еще молоды!")

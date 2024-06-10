"""
Множества sets.
Использовать для сравниния больших данных !
Работает в разы быстрее чем списки!
"""
#задание пустого множества.
my_set = set()
set_a = {1,2,3}
set_b = {4,5,6}
set_c = {4,5,3}

#создать множество из списка.
my_list = [1,2,3,4,5]
my_set_ = set(my_list)
print('Был список my_list:', my_list)
print('Получилось множество:',my_set_)

#  объединение двух множеств.
print(set_a | set_b)

set_d = set()
set_d |= set_a | set_b
print (set_d)

# union
my_set = set_a.union(set_b)
print('Union func my_set:', my_set)
print(my_set)

#update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x) 

# поиск пересечения. Различающихся элементов.
print(set_a & set_c)
print("intersection:",set_a.intersection(set_c))

set_z = set()
set_z = set_a.difference(set_c) # возвращает все элементы множества set_a которых нет в множестве set_c
print('set_z', set_z)

# добавление элемента
fruits = {"apple", "banana", "cherry"}
fruits2 = {"apple", "pineapple", "banana", "cherry"}
fruits.add("orange")
fruits.add("apple")
print(fruits)

# удаление элемента
fruits.discard("banana") 
print(fruits)
# очистить
fruits= fruits.clear()
print(fruits)

print('Разность множеств=============')
# удаление из множества всех элементов  совпадающих с множеством которое вычитаем. - или difference()
set_z = set_z.clear()
set_x = {1,2,3}
set_y = {3,4,5}
set_z = {2,3,(5,6),(6,5)}
print(set_x)
print(set_y)
print(set_z)
print(set_x - set_y - set_z)
print(set_x.difference(set_y,set_z))

#симметрическая разность. (выкинуть общие элементы и объеденить множества.)
print(set_x ^ set_y)
print(set_x.symmetric_difference(set_y))

# длина множества len()
print(len(set_x))

#создать копию множества. copy()
set_v = set_a.copy()
print(set_v)

#проверка наличия элемента
if 1 in set_a:
    print('Exist:', 1)
    
#сравнение множества
if set_a == set_y:
    print('Множества set_a и set_b равны')
else:
    print('Множества set_a и set_b не равны')
    
#issubset() проверят , является ли set 1 подмножеством set2. set1 должно входить в set 2 либо они должны быть идентичны.
a_set = {1,2,3,4}
b_set = {1,2}
print(b_set.issubset(a_set))
print(a_set.issubset(b_set))

#issuperset() проверяет включает ли в себя множество set1 множество set2 . set2 должно входить в set1 , либо они должны быть идентичны.
print(b_set.issuperset(a_set))
print(a_set.issuperset(b_set))

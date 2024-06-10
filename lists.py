print('Hello world!')

#Типы данных.
mystr = 'Моя строка'    #str
pi = 3,14       #float
my_int = 10     #int
mybool = True   #bool
# функции для изменения типа данных int(), float(), bool(), str()
print (round(42.4234, 2)) #округление числа до необходимого количества цифр после точки.

#индексация и срезы строк.
str_ = 'Hello'
print(str_[0])
print(str_[4])
print(str_[::2])
print(str_[::-1])

print('===============')
my_string = 'индекс'
print(my_string[0])
print(my_string[-6])
print(my_string[1:3])
print(my_string[0:4:2]) #срез с 0 по 3 включительно с шагом 2 .
print(my_string[3:])
print(my_string[:3])
print('===============')

word = 'testing'
if len(word) % 2 == 0:
    print(word[len(word) // 2-1:len(word) // 2+1])
else:
    print(word[len(word) // 2])

#списки list
name_list = []
user_data = ['Петров', 'Николай', 'Иванович']

my_list =[]
print(type(my_list))

languages = ['Python', 'Perl', 'Java', 'C', 'C++', 'JavaScript']

mystr = 'Сычев Владислав Викторович'
name_list = mystr.split()
print(name_list)

#срезы списов.
print(languages[0:3])
print(languages[-1])
print(languages[::-1])

#замена элементов списка.
languages[2] = 'Ruby'
languages[1:4:2] = ['C++', 'Java']
languages.append('Pascal') # добавить в конец элемент.
languages.insert(2,'Assembler') # добавить элемент на нужную позицию
languages.remove('Ruby') # удалить элемент
del languages[0:2]  #удалить элемент по индексу.
print(languages)
languages.pop() #удалить последний элемент списка.
#languages.clear()                    #полностью очистить список.
languages.append('JavaScript')
print(languages.count('JavaScript'))    #подсчитать количество элементов в списке.
languages2 = ['Bash','Haskel']
languages.extend(languages2)    #расширение одного списка другим.
new_list = languages +  languages2 #конкатенация двух списков и создание нового списка.
languages.reverse()
print(languages)
print(new_list)
# сортировка списков.
income_list = [13000,  14000, 14300, 15000, 13800, 14999, 15200, 15300]
income_list.sort()
print(income_list)
income_list.sort(reverse=True)
print(income_list)
#создание ссылки на один и тотже список.
a = [1,2,3]
b = a
b.append(4)
print(a)
print(b)
print(id(a))
print(id(b))
#создание списка на основе текущего списка.
a = [1,2,3]
b = a.copy()
b.append(4)
print(a)
print(b)
print(id(a))
print(id(b))

a = [1,2,3]
b = a[:]
b.append(4)
print(a)
print(b)
print(id(a))
print(id(b))

a = [1,2,3]
b = list(a)
b.append(4)
print(a)
print(b)
print(id(a))
print(id(b))

#минимальное / максимальное значение списка.
max_el = max(income_list)
print(max_el)
min_el = min(income_list)
print(min_el)
#суммирование всех элементов списка.
sum_list = sum(income_list)
print(sum_list)
# количество элементов списка.
len_list = len(income_list)
print(len_list)

#вложенные списки, извлечение по индексу.
my_list2 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print(my_list2[1][0])
print(my_list2[2][-1])


d = [1,2,3][1:]
print(len(d))


# кортежи.
user_data = ('Петров','Иванов','Сидоров')
print(type(user_data))

# разница в памяти которую занимает кортеж и список.
tuple_ = (1,2,3,4,5,6,7,8,9,10)
list_= [1,2,3,4,5,6,7,8,9,10]
print(tuple_.__sizeof__())
print(list_.__sizeof__())

#строки в кортеж и список.
some_str = 'Hello'
str_to_list = list(some_str)
print(str_to_list)
str_to_tuple = tuple(some_str)
print(str_to_tuple)

#список в кортеж и строку.
some_list = [1,2,3]
list_to_str = str(some_list)  #так лучше не делать - костыль!
print(list_to_str)

some_str_list = ['1','2','3']
str_list_to_str = ''.join(some_str_list)
print(str_list_to_str)

list_to_tuple = tuple(some_list)
print(list_to_tuple)

#множественное присваивание .
name, pro, salary = ('Mask','Developer',1000000)
print(name,pro,salary)


#алгоритм замены переменных местами. (на других языках !!!)
answer = 42
code = 4938493849

c = answer
answer = code
code = c
print(answer, code)

# на python делаем так.
answer, code = code, answer
print(answer,code)

# zip слияние объектов в список кортежей.
month_list = ['Jan','Feb','Mar']
income_list =  [13000,  14000,  14300]
salary_by_name = zip(month_list,income_list)
print(salary_by_name)   #итератор можно преобразовать в составной тип данных или пройтись по нему циклом.
print(list(salary_by_name))


# проверка элементов в списках , кортежах . in , not in
sea_animals = ['лебедь', 'бабайка', 'телепузик']
if 'щука' in sea_animals:
    print('Варим уху!')
else:
    print('Сегодня без ухи!')
    
#многомерные списки.
my_new_list = [[1,2,3,4],[4,5,6],4]
my_index = my_new_list.index(4); # узнать индекс элемента в списке.
print(my_index)
del my_new_list[0]; #удаление элемента по индексу. remove()
print(my_new_list)
my_new_list.append(5) #добавление элемента 
print(my_new_list)
my_count = my_new_list.count(5) # количество вхождений элементов в массив
print(my_count)
#reverse() разворачивает список.
#sorted(list) сортирует список.

#zip
list_1 = [1,2,3]
tuple_1 = ('A','B','C')
zip_object = zip(list_1,tuple_1)
print(list(zip_object))
if 'A' in list(zip_object):
    print('A exiest!')
#iterate zip object.
print('first time:')
for first,second in zip_object:
    print(first,second)
print('second time:')
for first,second in zip_object:
    print(first,second)
print('done')

# zip examle
fruits = ["apples","oranges","bananas","melons"]
prices = [20,10,5,15]
quantities = [5,7,3,4]

money_total = 0;
for fruit, price, quantity in zip(fruits,prices,quantities):
  #print(f"You bought {quantity} {fruit} for ${price*quantity}")
  money_total += price*quantity
  print ('You bought', quantity,  fruit, 'for $', price*quantity)
print('Total price:',money_total)




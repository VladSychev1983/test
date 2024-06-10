#однострочное тернарное выражение.
num = 6
print('Четное') if num % 2 == 0 else print('Нечетное')

a = 10 + 20;
b = a * 30
c = a/b;
print ('ответ:', c)

income_2021 = 100
income_2022 = 105.5
income_2023 = 105.5

print(income_2021 == income_2022)
print(income_2022 == income_2023)
# присваиваем результаты сравнения переменным.

comparison_1 = income_2021 >= income_2022
comparison_2 = income_2022 >= income_2023
print(comparison_1)
print(comparison_2)

# какое число соответствует символу.
print(ord('V'))
print(ord('l'))
print(ord('a'))
print(ord('d'))

print(ord('K'))
print(ord('l'))
print(ord('i'))
print(ord('m'))

name_1 = 'Vlad'
name_2 = 'Klim'
print(name_1 <= name_2)
print ("================")

a = 'Hello World!'
b = 'Hello World!\n'
c = a
print(id(a))
print(id(b))
print(id(c))
if id(a) == id(b):
    print('Id a and b differant!\n')
else:
    print('The same Ids!\n')

if a is b:
    print('Id a and b differant!\n')
else:
    print('The same Ids!\n')

#Логические операторы.
# not логическое не
print(not True)
print(not False)
print(not (5 == 10))
print(not ('abc' != 'bca'))
# and логическое И если один из операрандов False все выражение False.
a = 1
cond_1 = 0 < 4
cond_2 = 4 > a
print(cond_1 and cond_2)

str_1 = 'python'
str_2 =  'perl'
target_len = 5
print(len(str_1) > target_len and len(str_2) > target_len)



print(True and True or True and False or not True)

print(True and True or False or False)

print(True or False)

# вычисление високосного года.
year = int(input('Введите год:'))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Високосный год')
else:
    print('Обычный год')
 
 #остаток от деления.   
print(10%9)
    



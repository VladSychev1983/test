#отправляем в функцию переменную, список, кортеж , словарь  и обращаемся к ним.
def total(a, mylist, mytuple, mydict):
    print('a',a)
    #view list
    for item in mylist:
        print('item:',item)
    for single_item in mytuple:
        print('single_item:', single_item)
    
    for first_part,second_part in mydict.items():
        print(first_part,second_part)
    
a = 5
mylist =['volvo','mersedes','lada']
mytuple =('1','2','3','4')
mydict ={'1':'one','2':'two','3':'three'}

print(total(a,mylist,mytuple,mydict))

# Если нужно передать переменное число параметров используем * и ** перед аргументом.
print('============================')
def total(a=5, *numbers, **phonebook):
    print('a', a)
#проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)
#проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

print('==============')
def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        print(count,'+', number)
        count += number
        print(count,'+',extra_number)
        count += extra_number
        print(count)     
    print(count)
total(10, 1, 2, 3, extra_number=50)
#total(10, 1, 2, 3)

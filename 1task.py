seconds_per_hour = int(60*60)
print('The one hour consists of seconds:',seconds_per_hour)

seconds_per_day = int(seconds_per_hour * 24)
print('The one day consists of seconds:',seconds_per_day)

print(seconds_per_day/seconds_per_hour)
print(seconds_per_day//seconds_per_hour)

#str to list
mystr = "cat"
mystr_list = list(mystr)
print(mystr_list)

#tuple to list
mytuple = ('mazda','mersedes','toyta','gily','uaz patriot')
print(mytuple[-1])
print(type(mytuple))
mytuple_list = list(mytuple)
print(type(mytuple_list))
print(mytuple)
print(mytuple_list)

# list to tuple
new_tuple = tuple(mytuple_list)
print(new_tuple)

#string to list by "split"
mydate  = "2024-02-04"
mydate_list = mydate.split("-")
print(mydate_list)

#list to strin by "join"
list__ = ['Баба с','возу','кобыле', 'легче']
separator = " "
list__str = separator.join(list__)
print(list__str)

#check element in list with "in"
list_ = [1,2,3,4,5]
print(1 in list_)

if 1 in list_:
    print('1 exists in List')
else:
    print('1 No in List')

#from list of list  to list (самый простой способ изменить структуру списка)
my_list = [['Москва', 'Норильск'],['Санкт-Петербург','Пермь'],['Керчь', 'Геленджик']]
print(sum(my_list,[]))

#list comprehansion . Заполнить список четными значениями.
list_ = [i for i in range(11) if i % 2 ==0]
print(list_)

#как создать список списковв.
matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)




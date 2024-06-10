#######################
"""
x = 1
while x < 11:
    print(x)
    x += 1  #the same   x = x + 1
"""
#программа спрашивает числа у пользователя и после первого нуля выводит сумму чисел.
"""
sum_ = 0
number = 1
while number !=0:
    number = float(input('Введите число:'))
    sum_ +=  number
print(sum_)
"""
#######################
# гипотеза коллатца
number = int(input('Введите число:'))
counter = 0
while number != 1:
    if number % 2 == 0:
        number /= 2
    else:
        number = (number * 3 + 1) /2
    counter += 1
print(number)
print(counter)
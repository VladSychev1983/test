
def printMax(x,y):
    '''Программа выводит максимальное число из двух чисел.
    
    Оба значения должны быть целыми.
    '''
    x = int(x)
    y = int(y)
    if x > y:
        print (x, 'наибольшее')
    else:
        print(y, 'наибольшее')
printMax(3,5)
print(printMax.__doc__)
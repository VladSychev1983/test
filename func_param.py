def printMax(a,b):
    if a > b:
        print(a, "Максимальное");
    elif a == b:
        print(a, 'Равно', b);
    else:
        print(b,"Максимальное");
print('Введите 2 числа и я угадаю какое больше!')
a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
printMax(a,b)

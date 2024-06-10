def sayHello():
    print("Hello World!\n");
sayHello();

print('=========')
#Параментры функций.
def printMax(a, b):
    if a > b:
        print(a,'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b,'максимально')
printMax(6,4)

#lambda функция беземянная.
print("lambda функция\n")
double = lambda x: x*2
print(double(5))

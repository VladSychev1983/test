
def sum_func(x,y):
    z = x + y
    return z

sum_res = sum_func(10,20)
print(sum_res)

def check_num(x,y):
    if x > y:
        return 'x > y'
    elif x < y:
        return 'x < y'
    elif x == y:
        return 'x = y'
    else:
        return 'Ошибка!'
x = int(input('Введите число х:'))
y = int(input('Введите число y:'))
check_res = check_num(x,y)
print(check_res)


def fio(initials: list[str]) -> str:
    my_str = initials[0][0] + initials[1][0] + initials[2][0]
    return my_str

mylist = ['Иванов', 'Иван', 'Иванович']
res = fio(mylist)
print(res)
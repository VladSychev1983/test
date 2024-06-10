workday = 8
worktime = 0 
todo_list = [
    ["Разобрать почту", 1],
    ["Обзвонить клиентов", 2],
    ["Запланировать дела на завтра", 0.6],
    ["Сделать презентацию", 3],
    ["Созвон с командой", 0.5]
]
for dill, hour in todo_list:
    worktime += hour
    print(dill, hour)
print(worktime)
freetime = workday - worktime
freetime = round(freetime,1)
print(freetime)




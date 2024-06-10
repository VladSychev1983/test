boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
result = ''
#result_list = []
boys.sort()
girls.sort()
if len(boys) == len(girls):
    for boy,girl in zip(boys,girls):
#        result_list = []
#       result_list.append(boy + ' и ' + girl)
  #      result = ', '.join(result_list)
        result += boy + ' и ' + girl + ', '
    #result = result.strip(', ')
    result = result[0:-2]
else:
    result = 'Кто-то может остаться без пары!'
print(result)

#Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha
#Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha

"""
boys.sort()
girls.sort()
y = 0
result_list = []
if int(len(boys)) == int(len(girls)):
    for x in boys:
        result_list.append(f"{boys[y]} и {girls[y]}")
        y += 1
    result = ", ".join(result_list)
else:
    result = "Кто-то может остаться без пары!"
#return result

print(result)
"""
#result += f'{boy} и {girl}, '
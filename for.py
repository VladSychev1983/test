"""
company_name = 'Netology'
for letter in company_name:
    print(letter, end=' ')
    
"""    
## больше 100 киллограмм  на грузовой , меньше на легковой.
"""
weight_of_product = [10, 42.4, 243, 102.4 , 98, 92, 0.3, 15]
max_weight = 100
for weight  in weight_of_product:
    if weight < max_weight:
        print('Товар весит:', weight, 'и отправляется на легковой машине')
    else:
        print('Товар весит:', weight, 'и отправляется на грузовой машине')
"""
# найти все слова в строке которые длина которых больше определенного значения.
"""
text = 'Python - высокоуровневый язык программирования, ориентированный на повышение производительности разработчика и читаемости кода'
n = 6
words = []

for word in text.split():
    word = word.strip('.,!?-')
    if len(word) > n:
        words.append(word)
print(words)
"""
# перебор вложенных списков в списке. For с одной переменной.
"""
companies = [['Апельсин', 1.3],['Максисофт',1.5 ],['Головакнига',0.8],['Никола', 2.2]]
for company in companies:
    print ('Компания', company[0], 'имеет капитализацию', company[1], 'млн рупий')
"""
# перебор вложенных списков в списке. For с двумя переменными. (количество значений должно быть одинаковое.)
"""
companies = [['Апельсин', 1.3],['Максисофт',1.5 ],['Головакнига',0.8],['Никола', 2.2]]
for company, cap in companies:
    print ('Компания', company, 'имеет капитализацию', cap, 'млн рупий')
"""
#посчитать сумму элементов по диагонале в квадратной матрице.
data = [[13,25,23,34],
        [45,32,44,47],
        [12,33,23,95],
        [13,53,34,35]
        ]
sum_ = 0
index = 0
#index = -1  если считать по обратной диагонали.
for row in data:
    sum_ += row[index]
    index += 1
    #index -= 1
print(sum_)

#вывод теоремы пифагора.
for row in range(1,10):
    for col in range(1,10):
        print(row * col, end='\t')
    print()
    
#в списке со строками и числами просуммировать все четные числа.
some_els = [10,5,8,2,'abc',12,3]
result = 0
for el in some_els:
    if type(el) != int:
        print('Элемент', el, 'не является числом!')
        continue
    if el % 2 == 0:
        result += el
print('Сумма четных чисел:', result)




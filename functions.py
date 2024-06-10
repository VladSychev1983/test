#пример функции 
def square(number):
    result = number ** 2
    return result

result = square(5)
print(result)

#функция map , принимает функцию и элемент для обработки в этой функции (состовной объект)
#можно также передавать встроенные в python функции . Например sum.

prices = [[100,123,14],[303,23,534]]
def get_avg(list_):
    return sum(list_) / len(list_)
print(list(map(get_avg,prices)))

print(list(map(sum,prices)))

#анонимные lambda функции.
l_func = lambda prices: sum(prices) / len(prices)
print(l_func([1,20,21,33]))

print(list(map(lambda prices: sum(prices) / len(prices),prices)))

#filter функция. Пример ищем где присутствует "Россия"
geo_logs = [
    {'visit1': ['Курск','Россия']},
    {'visit2': ['Москва','Россия']},
     {'visit3': ['Париж','Франция']},
      {'visit4': ['Хургада','Египет']}
]
# простой перебор.
result = []
for log in geo_logs:
    if 'Россия' in list(log.values())[0]:
        result.append(log)
print(result)

#решение через filter в одну строку.
print(list(filter(lambda log: 'Россия' in list(log.values())[0], geo_logs)))









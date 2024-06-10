"""
Написать программу которая выводит список всех полиндромов из списка.
"""
phrases = [
           "нажал кабан на баклажан", 
           "дом как комод", 
           "рвал дед лавр", 
           "азот калий и лактоза",
           "а собака боса", 
           "тонет енот", 
           "карман мрак", 
           "пуст суп"
]
result = []
for phrase in phrases:
    clear_phrase = phrase.replace(" ", "")
    if clear_phrase == clear_phrase[::-1]:
        result.append(phrase)
print(result)
        
#s.strip()
#s.replace(" ", "")
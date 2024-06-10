''' программа проверки электронного адреса Email    
'''
email = input('Введите Email:')
if email.count('@') == 1 and email[0] != '@' and email.count('.') > 0 and email.rfind('.') > email.find('@') and email.count(' ') == 0:
    print('email valid ok!')
else:
    print('email invalid!')
    
#ищем индекс элемента @ он должен быть меньше индекса последнего вхождения элемента точка "."
#print(email.find('@')) 
#print(email.rfind('.'))

new_email = 'Helloworld@ya.ru'
print(new_email.count(' '))

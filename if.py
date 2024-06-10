number = 23;
guess = int (input('Угадайте число:'));
if guess == number:
    print ('Поздравляем Вы угадали число!,')
    print ('(хотя и не выйграли никакого приза!)');
elif guess < number:
    print ("Введеное число больше!");
else:
    print ("Введено число меньше!");
print ("Завершено");



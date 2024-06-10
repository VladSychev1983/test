#Напишите программу, которая проверяет логин (переменная login) и пароль (переменная password) пользователя. Если логин равен “admin” и пароль равен “password”,
#выведите сообщение «Добро пожаловать», иначе выведите сообщение «Доступ ограничен».
def check_auth(login: str, password: str):

    if # Здесь напишите свой код для проверки условия
        # В этом блоке напишите код, который выполнится, если условие True. Используйте result, как в задании выше
    else:
        # В этом блоке напишите код, который выполнится, если условие False. Используйте result, как в задании выше

    return result


if __name__ == '__main__':
    auth = check_auth('user', 'password')
    assert auth == 'Доступ ограничен', f'Получен неверный ответ: {auth}'
    print('Неверный login:', auth)

    auth = check_auth('admin', '123')
    assert auth == 'Доступ ограничен', f'Получен неверный ответ: {auth}'
    print('Неверный password:', auth)

    auth = check_auth('admin', 'password')
    assert auth == 'Добро пожаловать', f'Получен неверный ответ: {auth}'
    print('Верные login, password:', auth)

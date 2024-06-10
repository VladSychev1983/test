#можно задать последующим аргументам функции значения по умолчанию.
def say(message, times = 1):
    print(message * times)
say('Привет')
say('Мир', 5)

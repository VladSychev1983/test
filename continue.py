while True:
    s = input('Введите что-нибудь:')
    if s == 'выход':
        break
    if len(s) < 3:
        print('строка слишком коротка!')
        continue
    print("Введеная строка достаточной длины!")
print('Завершено')
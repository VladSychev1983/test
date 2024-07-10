import random
tasks = ['Создать группу в VK, получить Token группы внести изменения в settings.yaml', 
         'Спроектировать базу postgresql, расписать orm sqlalchemy в class/models.py, сделать pg_dump sql файл выложить в git',
         'Создать pip freeze requirments.txt требования к проекту.',
         'Документирование проекта README.md',
         'Работа с классом VK. hello_message() настроить взаимодействие с группой, создать класс VK , __init__',
         'Работа с классом VK. def get_data() метод принимает сообщения с данными из группы VK',
         'Работа с классом VK. def search_user() метод осуществляет поиск пользователей по заданным критериям в VK',
         'Работа с классом VK. def get_user_photo() метод получает и возращает три фотографии пользователя VK.',
         'Работа с классом VK. def send_found_users() метод возвращает найденных по запросу пользователей в группу VK.',
         'Работа с классом VK. def save_found_users() метод сохраняет в базу найденных по критериям пользователей.',
         'Работа с классом VK. def get_users_from_favorite() метод выводит список избранных из базы данных.',
         'Работа с классом VK. def send_users_from_favorite() метод отправляет в группу список избранных пользователей.',
         'Работа с классом VK. def next_user() метод переходит к следующему человеку из списка обнаруженных.',   
        ]   

developers = ['Vlad_sychev','Alex_serbin','Alex_petrunin']
for task in tasks:
     dev_index_list = [x for x in range(0,len(developers))]
     suffled_dev_index = sorted(dev_index_list, key=lambda x: random.random())
     shuffled_list = sorted(developers, key=lambda x: random.random())
     #print(f'{task} - {shuffled_list[random.choice(dev_index_list)]}')

result = {}
while tasks:
    task = tasks.pop()
    result[task] = random.choice(developers)
    if len(tasks) == 0:
        break
total_res = {}
developer_list = []
for task,dev in result.items():
    for dev_i in developers:
        if dev_i == dev:
            developer_list.append(dev_i)
        dev_count = developer_list.count(dev_i)
        total_res[dev_i] = dev_count
    print(f'{dev} - {task}')

print(f'Всего задач: {len(result)}')
for dev,counter in total_res.items():
    str_ = "".join(f'{dev} - {counter} ')
    print(str_, end="")
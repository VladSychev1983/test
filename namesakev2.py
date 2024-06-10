# -*- coding: utf-8 -*-
"""
Подсчитать тезок на каждом курсе.
На курсе Java-разработчик с нуля есть тёзки: Иван Бочаров, Иван Маркитан, ...
На курсе Fullstack-разработчик на Python есть тёзки: Александр Бардин, Александр Иванов, ...
На курсе Python-разработчик с нуля есть тёзки: Александр Бардин, Александр Ульянцев, ...
На курсе Frontend-разработчик с нуля есть тёзки: Александр Фитискин, Александр Шлейко, ...
"""
courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

all_list = []
for m in mentors:
    all_list.extend(m)

all_names_list = []
for mentor in all_list:
    name, fio = mentor.split(" ")
    all_names_list.append(name)
unique_names = sorted(set(all_names_list))  #список уникальных имен учителей.

courses_list = []
for course, mentor, duration in zip(courses, mentors, durations):
	course_dict = {"title":course, "mentors":mentor, "duration":duration}
	courses_list.append(course_dict)
#на каждом курсе в отдельности найди имена которые встречаются более 1 раза.
some_name_list = []
names = []

fio_java = []
fio_fs = []
fio_py = []
fio_front = []
result_list = [fio_java] + [fio_fs] + [fio_py] + [fio_front]
result_list_sorted = sorted(result_list)
for idx,course in enumerate(courses_list):
    for fio in course["mentors"]:
        name, surname = fio.split(" ")  
        names.append(name)
    for uname in unique_names:
        counter_name = 0
        for name in names:
            if uname == name:
                counter_name +=1
                #counter_name = names.count(name)
                if counter_name > 1 and uname not in some_name_list:
                #if counter_name > 1:
                    some_name_list.append(name)
    for fio in course["mentors"]:
        name,surname = fio.split(" ")
        if name in some_name_list:
            if idx == 0:
                fio_java.append(fio)
            elif idx == 1:
                fio_fs.append(fio)
            elif idx == 2:
                fio_py.append(fio)  
            else:
                fio_front.append(fio)
fio_java.sort()
fio_fs.sort()
fio_py.sort()
fio_front.sort()
result_list.sort()
for idx,course in enumerate(courses_list):
    print('На курсе',course["title"],'есть тезки:',', '.join(result_list_sorted[idx]))
    


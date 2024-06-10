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
unique_names = sorted(set(all_names_list))

courses_list = []

for course, mentor, duration in zip(courses, mentors, durations):
	course_dict = {"title":course, "mentors":mentor, "duration":duration}
	courses_list.append(course_dict)

same_name_list = []

names = []
for idx_course,mentor in enumerate(courses_list):
    for fio in courses_list[idx_course]["mentors"]:
        fio_index = courses_list[idx_course]["mentors"].index(fio)
        name, surname = fio.split(" ")
        names.append(name)
        #print(idx_course, fio_index, name)
        count_name = names.count(name)
        print(name,count_name)
        if count_name > 1:
            same_name_list.append([idx_course, fio])
            #same_name_list.append(name)
            #print(fio)
    
result_list = []
result_list_java = []
result_list_fs = []
result_list_python = []
result_list_front = []

for idx,fio in same_name_list:
    if idx == 0:
        result_list_java.append(fio)
    elif idx == 1:
        result_list_fs.append(fio)
    elif idx == 2:
        result_list_python.append(fio)
    else:
        result_list_front.append(fio)
result_list_java.sort()
result_list_fs.sort()
result_list_python.sort()
result_list_front.sort()
result_list = [result_list_java] + [result_list_fs] + [result_list_python] + [result_list_front]

print("==============")
print(result_list)

print("==============")
for idx,fio in enumerate(courses):
    print("На курсе", courses[idx], 'есть тезки:', ", ".join(result_list[idx]),)
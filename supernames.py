"""
Нужно найти учителей которые преподают более чем на 1 курсе.
Поиск делаем только по имени.
сравнить списки и вывести совпашие имена и пару курсов.
Вывод результата:

На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Антон, Евгений, Максим
На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: ...
На курсах 'Python-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: ...
На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: ...
На курсах 'Java-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: ...
На курсах 'Fullstack-разработчик на Python' и 'Frontend-разработчик с нуля' преподают: ...

"""

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

mentors_names = []
for m in mentors:
    for name in m:
        mentors_names.append(name[0:name.find(' ')])
#print(mentors_names)

pairs = []
course_names = []
for course, teacher_lists in zip(courses,mentors):
    set_names = set()
    for teacher in teacher_lists:
        name = teacher[0:teacher.find(' ')]
        set_names.add(name)
    course_names.append([course, list(set_names)])

print(course_names)
print("=======")

set_python_names = set(course_names[0][1])  #python
set_java_names = set(course_names[1][1]) #java
set_fullstack_names = set(course_names[2][1])   #fullstack
set_frontend_names = set(course_names[3][1]) #frontend

python_java_diff = set_python_names.intersection(set_java_names)
python_fs_diff = set_python_names.intersection(set_fullstack_names)
python_front_diff = set_python_names.intersection(set_frontend_names)
java_fs_diff = set_java_names.intersection(set_fullstack_names)
java_front_diff = set_java_names.intersection(set_frontend_names)
fs_front_diff = set_fullstack_names.intersection(set_frontend_names)

print('На курсах \'Python-разработчик с нуля\' и \'Java-разработчик с нуля\' преподают:', python_java_diff)
print('На курсах \'Python-разработчик с нуля\' и \'Fullstack-разработчик на Python\' преподают:', python_fs_diff)
print('На курсах \'Python-разработчик с нуля\' и \'Frontend-разработчик с нуля\' преподают:', python_front_diff)
print('На курсах \'Java-разработчик с нуля\' и \'Fullstack-разработчик на Python\' преподают:', java_fs_diff )
print('На курсах \'Java-разработчик с нуля\' и \'Frontend-разработчик с нуля\' преподают:', java_front_diff)
print('На курсах \'Fullstack-разработчик на Python\' и \'Frontend-разработчик с нуля\' преподают:', fs_front_diff )

      






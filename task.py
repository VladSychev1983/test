class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_to_lecturer:
                lecturer.grades_to_lecturer[course] += [grade]
            else:
                lecturer.grades_to_lecturer[course] = [grade]
    def __str__(self):
        return f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания: {self.avarage_score()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}'
    
    def avarage_score(self):
        grade_list = sum(list(self.grades.values()),[])
        return round(sum(grade_list) / len(grade_list),1)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_to_lecturer = {}

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avarage_score()}'
       
    def avarage_score(self):
        grade_list = sum(list(self.grades_to_lecturer.values()),[])
        return round(sum(grade_list) / len(grade_list),1)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Python','Git']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

#ставим оценки студентам
cool_reviewer = Reviewer('Bruce', 'Lee')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
print(best_student.grades)

#ставим оценки лекторам
cool_lecturer = Lecturer('Steve','Jobs')
cool_lecturer.courses_attached += ['Python']
best_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(cool_lecturer, 'Python', 8)
best_student.rate_hw(cool_lecturer, 'Python', 10)
print(cool_lecturer.grades_to_lecturer)

#печатаем ревьюверов
print(cool_reviewer)
#печатаем лекторов
print(cool_lecturer)
print(cool_lecturer.avarage_score())
# grade_list_list = list(cool_lecturer.grades_to_lecturer.values())
# grade_list = sum(grade_list_list,[])
# print(round(sum(grade_list) / len(grade_list),2))
#печатаем студентов
print(best_student)

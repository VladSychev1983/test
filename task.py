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
        
    def __sub__(self, other):
        return f'Средняя оценка {self.name} {self.surname} - {self.avarage_score()} а {other.name} {other.surname} - {other.avarage_score()}'

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
    
    def __sub__(self, other):
        return f'Средняя оценка лекторов: {self.name} {self.surname} - {self.avarage_score()} баллов | {other.name} {other.surname} - {other.avarage_score()} баллов'


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

def students_sum_score(students_list,course):
    sum_score = 0
    counter = 0
    for student in students_list:
        if course in student.courses_in_progress:
            counter += 1
            sum_score += sum(student.grades[course])
    return round(sum_score / counter, 1)

def lecturer_sum_score(lecturers_list,course):
    sum_score = 0
    counter = 0
    for lecturer in lecturers_list:
        if course in lecturer.courses_attached:
            counter += 1
            sum_score += sum(lecturer.grades_to_lecturer[course])
    return round(sum_score / counter, 1)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Python','Git']
bad_student = Student('Chu','Lee','ladyboy')
bad_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
soso_mentor = Mentor('Ugly', 'Habbit')
soso_mentor.courses_attached += ['Java']

#ставим оценки студентам
cool_reviewer = Reviewer('Bruce', 'Lee')
soso_reviewer = Reviewer('Arnold','Schwarzenegger')
cool_reviewer.courses_attached += ['Python']
soso_reviewer.courses_attached += ['Java']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(bad_student, 'Python', 2)
cool_reviewer.rate_hw(bad_student, 'Python', 5)
cool_reviewer.rate_hw(bad_student, 'Python', 3)
print(best_student.grades)
print(bad_student.grades)

#ставим оценки лекторам
cool_lecturer = Lecturer('Steve','Jobs')
bad_lecturer = Lecturer('Izya','Shniperson')
cool_lecturer.courses_attached += ['Python']
bad_lecturer.courses_attached += ['Python']
best_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(cool_lecturer, 'Python', 8)
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(bad_lecturer, 'Python', 2)
best_student.rate_hw(bad_lecturer, 'Python', 3)
best_student.rate_hw(bad_lecturer, 'Python', 1)
print(cool_lecturer.grades_to_lecturer)
print(bad_lecturer.grades_to_lecturer)

#печатаем ревьюверов
print(cool_reviewer)

#печатаем лекторов
print(cool_lecturer)
print(cool_lecturer.avarage_score())
print(best_student)

#сравниваем двух лекторов по среднему баллу.
print(cool_lecturer - bad_lecturer)

#сравниваем двух студентов по среднему баллу.
print(best_student - bad_student)

#подчитываем средную оценку по всем студентам в рамках конкретного курса.
students_list = [best_student,bad_student]
course = 'Python'
students_avarage_score = students_sum_score(students_list,course)
print(f'Общий средний балл по всем студентам курса {course} - {students_avarage_score} баллов')

#подсчитываем среднюю оценки за лекции всех лекторов в рамках курса.
lecturers_list = [cool_lecturer,bad_lecturer]
lecturers_avarage_score = lecturer_sum_score(lecturers_list,course)
print(f'Общий средний балл по всем лекторам курса {course} - {lecturers_avarage_score} баллов')
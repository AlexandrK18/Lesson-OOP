class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0
        
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_an_average_rating(self, course):
        sum_hw = sum(self.grades[course]) / len(self.grades[course])
        self.average_rating = sum_hw
        return self.average_rating

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.average_rating} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        else:
            return self.average_rating < other.average_rating

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = 0
    
    def get_an_average_rating(self, course):
        sum_hw = sum(self.grades[course]) / len(self.grades[course])
        self.average_rating = sum_hw
        return self.average_rating

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_rating < other.average_rating

class Reviewer(Mentor):
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

students = ['best_student', 'best_studen2']

def calc_as_hw(students, course):
    sum = (best_student.get_an_average_rating(course) + best_student2.get_an_average_rating(course)) / len(students)
    return sum

lecturers = ['cool_lecturer', 'cool_lecturer2']

def calc_as_lect(students, course):
    sum = (cool_lecturer.get_an_average_rating(course) + cool_lecturer2.get_an_average_rating(course)) / len(lecturers)
    return sum

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('James', 'Parker', 'your_gender')
best_student2.courses_in_progress += ['Python', 'Git']
best_student2.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer2 = Reviewer('Kelly', 'Collins')
cool_reviewer2.courses_attached += ['Git']
 
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(best_student2, 'Python', 10)
cool_reviewer.rate_hw(best_student2, 'Python', 9)
cool_reviewer.rate_hw(best_student2, 'Python', 9)
cool_reviewer.rate_hw(best_student2, 'Python', 10)

cool_reviewer2.rate_hw(best_student, 'Git', 10)
cool_reviewer2.rate_hw(best_student, 'Git', 9)
cool_reviewer2.rate_hw(best_student, 'Git', 9)
cool_reviewer2.rate_hw(best_student, 'Git', 10)

cool_reviewer2.rate_hw(best_student2, 'Git', 10)
cool_reviewer2.rate_hw(best_student2, 'Git', 9)
cool_reviewer2.rate_hw(best_student2, 'Git', 10)
cool_reviewer2.rate_hw(best_student2, 'Git', 10)

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_lecturer2 = Lecturer('Johnson ', 'Moralis')
cool_lecturer2.courses_attached += ['Python']
 
best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'Python', 10)

best_student.rate_lect(cool_lecturer2, 'Python', 10)
best_student.rate_lect(cool_lecturer2, 'Python', 10)
best_student.rate_lect(cool_lecturer2, 'Python', 9)
best_student.rate_lect(cool_lecturer2, 'Python', 10)

best_student2.rate_lect(cool_lecturer, 'Python', 9)
best_student2.rate_lect(cool_lecturer, 'Python', 10)
best_student2.rate_lect(cool_lecturer, 'Python', 10)
best_student2.rate_lect(cool_lecturer, 'Python', 10)

best_student2.rate_lect(cool_lecturer2, 'Python', 10)
best_student2.rate_lect(cool_lecturer2, 'Python', 9)
best_student2.rate_lect(cool_lecturer2, 'Python', 9)
best_student2.rate_lect(cool_lecturer2, 'Python', 10)

print(best_student.grades)
print(best_student2.grades)
print(cool_lecturer.grades)
print(cool_lecturer2.grades)

print(best_student.get_an_average_rating('Python'))
print(best_student2.get_an_average_rating('Python'))
print(cool_lecturer.get_an_average_rating('Python'))
print(cool_lecturer2.get_an_average_rating('Python'))

print(cool_reviewer)
print(cool_reviewer2)
print(cool_lecturer)
print(cool_lecturer2)
print(best_student)
print(best_student2)

print(best_student < best_student2)
print(cool_lecturer < cool_lecturer2)

print(calc_as_hw(students, 'Python'))
print(calc_as_lect(lecturers, 'Python'))

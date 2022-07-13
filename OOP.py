class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, mark):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            lecturer.grades[course] = lecturer.grades.get(course, []) + [mark] 
        else:
            return 'Ошибка'

    def __get_avrg_grade(self):
        all_grades = sum(self.grades.values(), [])
        if len(all_grades) != 0:
            avrg_grade = sum(all_grades) / len(all_grades)
            return avrg_grade
        else:
            return 'нет оценок'


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.__get_avrg_grade()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.__get_avrg_grade() < other.__get_avrg_grade()

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__get_avrg_grade() == other.__get_avrg_grade()

    def __le__(self, other):
        if isinstance(other, Student):
            return self.__get_avrg_grade() <= other.__get_avrg_grade()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress \
                and isinstance(self, Reviewer):
            student.grades[course] = student.grades.get(course, []) + [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __get_avrg_grade(self):
        all_grades = sum(self.grades.values(), [])
        if len(all_grades) != 0:
            avrg_grade = sum(all_grades) / len(all_grades)
            return avrg_grade
        else:
            return 'нет оценок'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__get_avrg_grade()}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.__get_avrg_grade() < other.__get_avrg_grade()

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.__get_avrg_grade() == other.__get_avrg_grade()

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.__get_avrg_grade() <= other.__get_avrg_grade()


class Reviewer(Mentor):

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def avrg_by_cours(students_list, cours):
    all_marks = []
    for student in students_list:
        all_marks += student.grades[cours]
    return sum(all_marks) / len(all_marks) if len(all_marks) != 0 else 'оценок за курс не выставлялось'   



best_student = Student('Ivan', 'Ivanov', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 20)
cool_reviewer.rate_hw(best_student, 'Git', 30)
print(best_student)
print()

best_student2 = Student('Petr', 'Petrov', 'male')
best_student2.courses_in_progress += ['Python', 'Java', 'C++']
cool_reviewer2 = Reviewer('Some2', 'Buddy2')
cool_reviewer2.courses_attached += ['Python', 'Java', 'C++']
cool_reviewer2.rate_hw(best_student2, 'Python', 10)
cool_reviewer2.rate_hw(best_student2, 'Java', 40)
cool_reviewer2.rate_hw(best_student2, 'C++', 5)
print(best_student2)
print()
print(cool_reviewer2)
print()

cool_Lecturer = Lecturer('Some3', 'Buddy3')
cool_Lecturer.courses_attached += ['Python', 'Java', 'C++']
print(cool_Lecturer.rate_hw(best_student2, 'Python', 10))  # ошибка, оценка не добавляется, лектор не может ставить оценки
best_student.rate_lecturer(cool_Lecturer, 'Python', 10)
best_student2.rate_lecturer(cool_Lecturer, 'Java', 20)
print(cool_Lecturer)
print()
cool_Lecturer2 = Lecturer('Some4', 'Buddy4')
cool_Lecturer2.courses_attached += ['Python', 'Java', 'C++']
best_student.rate_lecturer(cool_Lecturer2, 'Python', 3)
best_student2.rate_lecturer(cool_Lecturer2, 'Java', 33)
print(cool_Lecturer2)
print('\nоператоры сравнения для студентов')

print(best_student == best_student2)
print(best_student < best_student2)
print(best_student >= best_student2)
print('\nоператоры сравнения для лекторов')
print(cool_Lecturer2 == cool_Lecturer)
print(cool_Lecturer2 < cool_Lecturer)
print(cool_Lecturer2 >= cool_Lecturer)
print('\nдоп. функция - средняя оценка по курсу')

print(avrg_by_cours([best_student,best_student2], 'Python'))  # средняя оценка по курсу

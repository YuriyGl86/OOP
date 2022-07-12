class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, mark):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            lecturer.marks[course] = lecturer.marks.get(course, []) + [mark]  # ---
        else:
            return 'Ошибка'

    def get_avrg_grade(self):
        all_grades = sum(self.grades.values(), [])
        avrg_grade = sum(all_grades) / len(all_grades)
        return avrg_grade

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.get_avrg_grade()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_avrg_grade() < other.get_avrg_grade()

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_avrg_grade() == other.get_avrg_grade()

    def __le__(self, other):
        if isinstance(other, Student):
            return self.get_avrg_grade() <= other.get_avrg_grade()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and isinstance(
                self, Reviewer):
            student.grades[course] = student.grades.get(course, []) + [grade]  # ---
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_avrg_grade(self):
        all_grades = sum(self.grades.values(), [])
        avrg_grade = sum(all_grades) / len(all_grades)
        return avrg_grade

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_avrg_grade()}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avrg_grade() < other.get_avrg_grade()

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avrg_grade() == other.get_avrg_grade()

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avrg_grade() <= other.get_avrg_grade()


class Reviewer(Mentor):

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Ivan', 'Ivanov', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 20)
cool_mentor.rate_hw(best_student, 'Git', 30)
print(best_student)
print()

best_student2 = Student('Petr', 'Petrov', 'male')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Java', 'C++']
cool_mentor2 = Reviewer('Some2', 'Buddy2')
cool_mentor2.courses_attached += ['Python', 'Java', 'C++']
cool_mentor2.rate_hw(best_student2, 'Python', 10)
cool_mentor2.rate_hw(best_student2, 'Java', 40)
cool_mentor2.rate_hw(best_student2, 'C++', 5)
print(best_student2)
print()

cool_mentor3 = Lecturer('Some3', 'Buddy3')
cool_mentor3.courses_attached += ['Python', 'Java', 'C++']
print(cool_mentor3.rate_hw(best_student2, 'Python', 10))  # ошибка, лектор не может давать оценок

print(best_student == best_student2)
print(best_student < best_student2)
print(best_student >= best_student2)
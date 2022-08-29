class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lect_rate(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses):
            if course in lecturer.courses_grades:
                lecturer.courses_grades[course] += [grade]
            else:
                lecturer.courses_grades[course] = [grade]
        else:
            return 'Ошибка'


    def _midgrade(self):
        grades_list = []
        for grades in self.grades.values():
            for grade in grades:
                grades_list.append(grade)
            if len(grades_list) == 0:
                self.midgrade = 0
            else:
                self.midgrade = sum(grades_list) / len(grades_list)
            return self.midgrade


    def __lt__(self, other):
        if isinstance(other, Student):
            return self.midgrade < other.midgrade
        else:
            return 'Ошибка!'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self._midgrade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses = []
        self.courses_grades = {}
        self.grades = {}

    def _midgrade(self):
        grades_list = []
        for grades in self.courses_grades.values():
            for grade in grades:
                grades_list.append(grade)
        if len(grades_list) == 0:
            self.midgrade = 0
        else:
            self.midgrade = sum(grades_list) / len(grades_list)
        return self.midgrade


    def __str__(self):
        return(f'Имя: {self.name}\n'
              f'Фамилия: {self.surname}'
              f'Средняя оценка за лекции: {self._midgrade()}\n')

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses = []
        self.courses_grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return(f'Имя {self.name}\n'
              f'Фамилия {self.surname}\n')

#reviewer1 = Reviewer('Андрей', 'Вышлов')
#print(reviewer1)

student1 = Student('Tom', 'Ford', 'Man')
student1.courses_in_progress = ['Python', 'C++', 'C#']
student1.finished_courses = ['Java', 'Math', 'SQL']

student2 = Student('Shurik', 'Kuznetcov', 'Man')
student1.courses_in_progress = ['Python']
student1.finished_courses = ['Java', 'Math', 'SQL', 'C++', 'C#']

lecturer1 = Lecturer('Jack', 'Vorobey')
lecturer1.courses = ['Python', 'SQL']

lecturer2 = Lecturer('Tony', 'Stark')
lecturer2.courses = ['Java', 'Math', 'C++', 'C#']

reviewer1 = Reviewer('Oleg', 'Tinkov')
reviewer1.courses = ['SQL', 'Python', 'C++']

reviewer1.rate_hw(student2,'SQL', 10)
reviewer1.rate_hw(student2,'SQL', 4)
reviewer1.rate_hw(student2,'C++', 5)
reviewer1.rate_hw(student1,'Python', 7)
reviewer1.rate_hw(student1,'SQL', 1)
reviewer1.rate_hw(student1,'Python', 10)

reviewer2 = Reviewer('Andrey', 'Vyshlov')
reviewer2.courses_attached = ['Java', 'C#']

student1.lect_rate(lecturer1,'SQL', 7)
student2.lect_rate(lecturer1,'SQL', 5)
student1.lect_rate(lecturer2,'Math', 3)
student2.lect_rate(lecturer2,'Math', 10)


print(student1)
print(student2)

print(lecturer1)
print(lecturer2)

print(reviewer1)
print(reviewer2)

print(student2 > student1)
print(lecturer2 > lecturer1)

students_list = [student1,student2]
lecturers_list = [lecturer2,lecturer1]
courses = ['SQL', 'Math', 'Python', 'C++', 'C#', 'Java']


def student_midgrades(students, course):
    all_course_grades = []
    for student in students:
        for grade in student.grades.get(course):
            all_course_grades += [grade]
    mid_grade = sum(all_course_grades) / len(all_course_grades)
    print(f'Средняя оценка за курс {course}: {mid_grade}')


def lecturer_midgrades(lecturers, course):
    all_course_grades = []
    for lecturer in lecturers:
        for grade in lecturer.grades.get(course):
            all_course_grades += [grade]
    mid_grade = sum(all_course_grades) / len(all_course_grades)
    print(f'Средняя оценка за курс {course}: {mid_grade}')


student_midgrades(students_list,courses[1])
lecturer_midgrades(students_list,courses[3])











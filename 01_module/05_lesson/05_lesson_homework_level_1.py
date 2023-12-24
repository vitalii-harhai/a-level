# Створити словник оцінок передбачуваних студентів (Ключ – ПІ студента, значення – список оцінок студентів).
# Знайти найуспішнішого і самого слабенького за середнім балом.

def calculate_average_grade(dict_students: dict) -> (list, float):
    average_grade_list = []  # список для кортежей (студент, средняя оценка)
    for name, grades in dict_students.items():
        average_grade_student = 0
        for item in grades:
            average_grade_student += item  # суммируем сумму всх оценок студента
        average_grade_for_student = round(average_grade_student / len(grades), 1)  # вычисляем среднюю по студенту
        average_grade_list.append((name, average_grade_for_student))  # добавляем кортеж в список студентов
    average_grade_for_group = 0
    for i in average_grade_list:  # в кортежах по второму элементу суммируем оценки студентов
        average_grade_for_group += i[1]
    average_grade_for_group = round(average_grade_for_group / len(average_grade_list), 1)
    return average_grade_list, average_grade_for_group


def max_average_student(list_students: list[str, float]):
    # ищем максимум по второму элементу кортежей (студент, оценка)
    max_student_grade = max(list_students, key=lambda x: x[1])
    return max_student_grade


def min_average_student(list_students: list[str, float]):
    # ищем минимум по второму элементу кортежей (студент, оценка)
    min_student_grade = min(list_students, key=lambda x: x[1])
    return min_student_grade


students = {
    'Melnyk Artem': [6, 7, 9, 6, 7, 3, 5, 10, 3, 11, 1],
    'Shevchenko Oleksandr': [10, 1, 5, 9, 3, 12, 11, 1, 2, 6, 5],
    'Kovalenko Anna': [2, 7, 11, 6, 5, 4, 10, 12, 11, 8, 10],
    'Bondarenko Sofiya': [6, 8, 8, 1, 8, 6, 5, 12, 10, 6, 5],
    'Boiko Mariya': [2, 10, 8, 5, 2, 10, 9, 8, 7, 11, 1],
    'Tkachenko Maksym': [10, 1, 10, 8, 6, 3, 4, 2, 10, 4, 10],
    'Kravchenko Viktoriya': [7, 8, 2, 2, 2, 5, 9, 11, 3, 3, 3],
    'Kovalchuk Bohdan': [11, 12, 7, 5, 1, 2, 11, 6, 9, 4, 1],
    'Oliinyk Veronika': [11, 9, 7, 10, 5, 12, 9, 8, 5, 9, 9],
    'Shevchuk Nazar': [3, 7, 2, 7, 9, 9, 1, 1, 5, 12, 1],
    'Polishchuk Dmytro': [3, 7, 12, 2, 9, 12, 5, 12, 1, 4, 10],
    'Ivanova Polina': [4, 7, 5, 7, 2, 3, 7, 8, 12, 1, 2],
    'Tkachuk Volodymyr': [11, 10, 11, 7, 8, 3, 2, 10, 4, 1, 1],
    'Savchenko Mykola': [5, 10, 8, 6, 10, 2, 6, 1, 5, 8, 4]
}

list_students_with_average_grade = calculate_average_grade(students)[0]
print(list_students_with_average_grade)

print(f'Середній бал по групі становить - {calculate_average_grade(students)[1]}')
print(f'Студент з максимальним балом є {max_average_student(list_students_with_average_grade)[0]} з балом '
      f'{max_average_student(list_students_with_average_grade)[1]}')
print(f'Студент з мінімальним балом є {min_average_student(list_students_with_average_grade)[0]} з балом '
      f'{min_average_student(list_students_with_average_grade)[1]}')

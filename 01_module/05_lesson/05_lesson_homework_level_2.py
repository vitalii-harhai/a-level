# Створити структуру даних для студентів з імен та прізвищ, можна випадкових. Придумати структуру даних, щоб вказувати,
# у якій групі навчається студент (Групи Python, FrontEnd, FullStack, Java). Студент може навчатися у кількох групах.
# Потім вивести:
# студентів, які навчаються у двох та більше групах
# студентів, які не навчаються на фронтенді
# студентів, які вивчають Python або Java

students = {
    'Melnyk Artem': ['Python', 'FrontEnd', 'FullStack', 'Java'],
    'Shevchenko Oleksandr': ['FrontEnd'],
    'Kovalenko Anna': ['Python'],
    'Bondarenko Sofiya': ['Java'],
    'Boiko Mariya': ['Python', 'FrontEnd', 'FullStack'],
    'Tkachenko Maksym': ['Java'],
    'Kravchenko Viktoriya': ['FrontEnd'],
    'Kovalchuk Bohdan': ['FullStack'],
    'Oliinyk Veronika': ['Python', 'Java'],
    'Shevchuk Nazar': ['FrontEnd', 'FullStack'],
    'Polishchuk Dmytro': ['FullStack', 'Java'],
    'Ivanova Polina': ['Python', 'Java'],
    'Tkachuk Volodymyr': ['FrontEnd', 'FullStack'],
    'Savchenko Mykola': ['FullStack']
}

print('*' * 50)
print('Студенти, які навчаються у двох та більше групах')
print('*' * 50)
s = filter(lambda x: len(x[1]) >= 2, students.items())  # фильтруем по максимальному размеру 2-го элемента кортежей
for i in s:
    print(i[0])

print('*' * 50)
print('Студенти, які не навчаються на фронтенді')
print('*' * 50)
s = filter(lambda x: 'FrontEnd' not in x[1], students.items())  # фильтруем по кортежам, где во 2-м элементе нет фронтенда
for i in s:
    print(i[0])

print('*' * 50)
print('Студенти, які вивчають Python або Java')
print('*' * 50)
s = filter(lambda x: 'Python' in x[1] or 'Java' in x[1], students.items())  # фильтруем по кортежам, где во 2-м элементе есть пайтон или ява
for i in s:
    print(i[0])

# это я уже от себя написал для фильтрации только по одному элементу
print('*' * 50)
print('Студенти, які вивчають тільки Python')
print('*' * 50)
s = filter(lambda x: ['Python'] == x[1], students.items())
for i in s:
    print(i)

# Задача 2. Бриллиант

count = 1
while True:
    user_number = int(input('Enter the odd number: '))
    if user_number % 2:
        break
    elif count > 2:
        print('Это такое число, которое делится с остатком на 2!')
    else:
        print('Enter нечетное число!!!!')
        count += 1

#ВАРИАНТ 1 с помощью флага Reverse (находим самую большую линию, это введенное число, и считаем вниз)
#Пробелы считаем число - количество звездочек и делим на 2
star = 1
reverse = False

for i in range(1, user_number + 1):
    space = int((user_number - star) / 2)
    print(f"{' ' * space}{'*' * star}")
    if not reverse:
        star += 2
    else:
        star -= 2
    if star == user_number:
        reverse = True

# ВАРИАНТ 2 с помощью нахождения средней линии (находим среднюю линия и считаем вниз)
# Пробелы считаем с помощью метода строки center и передаем туда ширину строки т.е. наше число

hash_tag = 1

for i in range(1, user_number + 1):
    spase = int(user_number - hash_tag)
    draw_line = hash_tag * '#'
    print(draw_line.center(user_number))
    if i < (user_number + 1) / 2:
        hash_tag += 2
    else:
        hash_tag -= 2


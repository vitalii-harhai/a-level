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

# ВАРИАНТ 1 с помощью флага Reverse (находим самую большую линию, это введенное число, и считаем вниз)

star = 1
reverse = False

for i in range(1, user_number + 1):
    space = int((user_number - star) / 2)
    print(f"{' ' * space}{'*' * star}")
    if not reverse:  # если реверса нет считаем вверх
        star += 2
    else:  # если реверс считаем вниз
        star -= 2
    if star == user_number:  # переключаем флаг на обратно
        reverse = True
# подводим итоги - range нам дает 1, 2, 3, 4, 5, 6, 7, 8 (мы кстати нигде переменную i не использовали)
# а переменная star 1, 3, 5, 7, 5, 3, 1
# ПЕРЕКЛЮЧЕНИЕ - на количестве символов *


# ВАРИАНТ 2 с помощью нахождения средней линии (находим среднюю линия и считаем вниз)

hash_tag = 1

for i in range(1, user_number + 1):
    draw_line = hash_tag * '#'
    print(draw_line.center(user_number))
    if i < (user_number + 1) / 2:  # здесь мы ищем среднюю самую большую линию
        hash_tag += 2
    else:
        hash_tag -= 2

# подводим итоги - range нам дает 1, 2, 3, 4, 5, 6
# а переменная hash_tag 1, 3, 5, 3, 1
# ПЕРЕКЛЮЧЕНИЕ - на средней строке

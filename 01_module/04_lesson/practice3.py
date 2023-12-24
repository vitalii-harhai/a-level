# Задача 3. Файл-тест.

with open('practice3.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        line_1 = line.split(';')[0]  # строка чисел
        line_2 = line.split(';')[1]  # строка результатов для проверки
        current_sum = 0
        count = 0
        for c in line_1:  # считаем количество и сумму в первой строке
            if c.isdigit():
                current_sum += int(c)
                count += 1
        check_number = []
        for c in line_2:
            if c.isdigit():
                check_number.append(int(c))  # собираем числа для проверки
        # делаем проверку
        check = True if current_sum // count == check_number[0] and current_sum % count == check_number[1] else False
        print(f'{line} - {check}')

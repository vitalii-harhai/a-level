# Задача 3. Файл-тест.

with open('practice3.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        line_1 = line.split(';')[0]
        line_2 = line.split(';')[1]
        current_sum = 0
        count = 0
        for c in line_1:
            if c.isdigit():
                current_sum += int(c)
                count += 1
        check_number = []
        for c in line_2:
            if c.isdigit():
                check_number.append(int(c))
        check = True if current_sum // count == check_number[0] and current_sum % count == check_number[1] else False
        print(f'{line} - {check}')



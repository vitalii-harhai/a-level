# Переробити другу задачу так, щоб результат писався в інший файл. Додаємо list comprehension, map та інші свіжеотримані
# знання до виконання завдання.
def fizz_buzz_string(fizz: int, buzz: int, end_number: int) -> str:
    fizz_buzz_string = ''
    for i in range(1, end_number + 1):
        if not i % fizz and not i % buzz:
            fizz_buzz_string += ' FB'
        elif not i % buzz:
            fizz_buzz_string += ' B'
        elif not i % fizz:
            fizz_buzz_string += ' F'
        else:
            fizz_buzz_string += f' {i}'
    return fizz_buzz_string.strip()


def get_number_from_string(number_string: str) -> list[int]:
    # переделано с простого перебора символов на использование list comprehension
    number_string = number_string.strip().split()
    number_list = [int(i) for i in number_string]
    return number_list


with open('level_2.txt', 'r') as file_read, open('level_3.txt', 'w') as file_write:
    # переделано с простого перебора строк на использование map и list comprehension
    numbers_from_file = map(get_number_from_string, file_read)
    strings_to_write = [fizz_buzz_string(s[0], s[1], s[2]) + '\n' for s in numbers_from_file]
    file_write.writelines(strings_to_write)

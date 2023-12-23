# Написати fizzbuzz для 20 комплектів по три числа, які записані в файл. Читайте із файлу перший рядок з трьома числами,
# беріть із нього числа, рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком і так до кінця файла.

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
    number_list = []
    number_string = number_string.strip().split()
    for i in number_string:
        number_list.append(int(i))
    return number_list


with open('level_2.txt', 'r') as file:
    for file_string in file:
        get_numbers = get_number_from_string(file_string.strip())
        get_fizz_buzz = fizz_buzz_string(get_numbers[0], get_numbers[1], get_numbers[2])
        print(get_fizz_buzz)

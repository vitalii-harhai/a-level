# Завдання 2
# Написати функцію, яка буде підносити число у квадрат. Написати другу, яка буде перевіряти, чи є число простим.
# Потрібно видрукувати в головній програмі квадрати усіх простих чисел зі списку від 0 до 50 за допомогою map

def number_squared(input_number: int) -> int:
    """
    Square a number
    :param input_number: number
    :return: number ** 2
    """
    return input_number ** 2


def is_prime_number(input_number: int) -> bool:
    """
    Check is number prime?
    :param input_number: number for check
    :return: True - if number is prime, False - if number complex
    """
    number_divisors = []  # делители числа
    is_prime = False
    for i in range(2, input_number + 1):  # получаем все делители числа без остатка
        if not input_number % i:
            number_divisors.append(i)
    if len(number_divisors) == 1:  # если число делитель один, это простое число
        is_prime = True
    return is_prime


# for i in range(51):

numbers = filter(lambda x: is_prime_number(x), range(51))  # фильтруем 0-50 где число элемент == простое
numbers = map(number_squared, numbers)  # применяем функцию квадрата к каждому числу

for i in numbers:
    print(i, end=' ')

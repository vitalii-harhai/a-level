# Завдання 1
# Написати 2 функції. Перша функція прийматиме рядок та приводитиме його до нижнього регістру.
# Друга функція прийматиме рядок та приводитиме його до верхнього регістру.
# Головна програма має застосовувати обидві функції до списку рядків за допомогою map, для кожного з рядків,
# та друкувати результат.


def string_to_lower_case(input_string: str) -> str:
    """
    Convert all symbol of string to lower case
    :param input_string: string for conversion
    :return: string with symbols in lower case
    """
    output_string = ''
    for symbol in input_string:
        output_string += symbol.lower()
    return output_string


def string_to_upper_case(input_string: str) -> str:
    """
    Convert all symbol of string to upper case
    :param input_string: string for conversion
    :return: string with symbols in upper case
    """
    output_string = ''
    for symbol in input_string:
        output_string += symbol.upper()
    return output_string


test_list_string = [
    'As an unperfect actor on the stage',
    'Who with his fear is put beside his part',
    'Or some fierce thing replete with too much rage',
    'Whose strength"s abundance weakens his own heart.'
]

# print strings in lower case
result = map(string_to_lower_case, test_list_string)
for i in result:
    print(i)

# print strings in upper case
result = map(string_to_upper_case, test_list_string)
for i in result:
    print(i)

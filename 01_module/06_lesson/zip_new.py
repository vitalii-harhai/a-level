# Знайомимось з zip функцією, пробуємо написати свій власний zip

def my_zip(*args):
    min_iterable_object = min(args, key=lambda x: len(x))  # получаем самый короткий объект из кортежа объектов
    iterable_objects = []
    for i in args:
        if not isinstance(i, dict):
            iterable_objects.append(i)
        else:
            iterable_objects.append(list(i.keys()))  # если это словарь, переводим в список ключей
    item = 0
    while item < len(min_iterable_object):  # итерируемся до длины самого короткого объекта
        # применяя map получаем 0-й элемент, потом первый и тд для всех последовательностей и переводим в tuple
        yield tuple(map(lambda x: x[item], iterable_objects))
        item += 1


#  тестируем на iterable объектах
a = [1, 2, 3, 4, 5, 6, 7]
b = ('A', 'B', 'C', 'D')
c = 'qwerty'
d = {'key1': 34, 'key2': 43, 'key3': 22, 'key4': 55, 'key5': 22}
e = range(10)
with open('test.txt', 'r') as file:
    f = file.read()

test = my_zip(a, b, c, d, e, f)

# проверяем итерирование
for y in test:
    print(y)

# проверяем метод __next__
# но есть нюанс, функция уже пустая, поэтому вызываем ее еще раз
test = my_zip(a, b, c, d, e, f)
print('__next__')
print(test.__next__())
print(test.__next__())
print(test.__next__())
print(test.__next__())
# а здесь получаем исключение StopIteration
print(test.__next__())


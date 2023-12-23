# LEVEL 1

# Кожен пише суму списку за допомогою for та while

my_list = [45, 'a', 50, 5, 20, 's']

sum_list = 0

for i in my_list:
    if type(i) is int:
        sum_list += i

print(f'Loop for - {sum_list}')

s = 0
length_list = len(my_list)

sum_list = 0

while s < length_list:
    if type(my_list[s]) is int:
        sum_list += my_list[s]
    s += 1

print(f'Loop while - {sum_list}')

# Написати програму, яка виводить сама себе

with open('03_lesson_homework_exercise.py', 'r') as file:
    file_text = file.read()

print('Text file')
print('-' * 50)
print(file_text)
print('-' * 50)

file_text = ''

# Написати програму, яка виводить саму себе задом наперед

with open('03_lesson_homework_exercise.py', 'r') as file:
    file_text = file.read()

print('Text file reverse')
print('-' * 50)
print(file_text[::-1])
print('-' * 50)

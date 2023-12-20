# LEVEL 1

# 1. Перевірити, чи є введене число парним.
user_number = int(input('Enter the number: '))

if user_number % 2:
    print(f'# 1. Введене число {user_number} є непарним')
else:
    print(f'# 1. Введене число {user_number} є парним')

# 2. Перевірити, чи є число не парним, ділиться чи на три і на п'ять одночасно, але так, щоб не ділитися на 10.
if user_number % 2 and (not user_number % 3 or not user_number % 5) and user_number % 10:
    print(f'# 2. {user_number} оце і є те число')
else:
    print('# 2. Це якесь інше число')

# 3. Ввести число, вивести усі його дільники
numbers = []
for i in range(1, user_number + 1):
    if not user_number % i:
        numbers.append(i)
message = '-'
for i in numbers:
    message += f' {i}'
print(f'# 3. Дільниками числа {user_number} є {message}')

# 4. Ввести число, вивести його розряди та їх множники.
prime_numbers = []
for i in range(2, user_number + 1):
    ostatok = []
    for n in range(2, i):
        if i % n:
            ostatok.append(True)
        else:
            ostatok.append(False)
    if all(ostatok):
        prime_numbers.append(i)

division_remainder = user_number
mnozhnyky = []

while division_remainder != 1:
    for i in prime_numbers:
        if not division_remainder % i:
            division_remainder /= i
            mnozhnyky.append(i)
            break

bit = 1
while True:
    if user_number // 10 ** bit == 0:
        break
    else:
        bit += 1

message = '-'
for i in mnozhnyky:
    message += f' {i}'
print(f'# 4. Множниками числа {user_number} є {message}, число {user_number} має {bit} розрядів.')

# LEVEL 3

# FIZZ-BUZZ

fizz = int(input('Enter the fizz number like integer: '))
buzz = int(input('Enter the buzz number like integer: '))
end_number = int(input('Enter the end number like integer: '))

message_fizz_buzz = ''

for i in range(1, end_number + 1):
    if not i % fizz and not i % buzz:
        message_fizz_buzz += ' FB'
    elif not i % buzz:
        message_fizz_buzz += ' B'
    elif not i % fizz:
        message_fizz_buzz += ' F'
    else:
        message_fizz_buzz += f' {i}'

print(message_fizz_buzz)

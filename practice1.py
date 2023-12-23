import math

# Вариант 1 с применение модуля math округления вверх

floors = 5
apartments_on_floor = 3
number = 59

podjezd = math.ceil(number / (floors * apartments_on_floor))
etaznost = math.ceil((number - (podjezd - 1) * floors * apartments_on_floor) / apartments_on_floor)

print(f'Номер квартиры - {number}, подъезд - {podjezd}, этаж - {etaznost}')


# Вариант 2

numbers_apartment_at_floor = 3
floors = 5
apartment = 59

# 3 квартиры на этаже 15 в подъезде, 1 подъезд 1 - 15, 2 подъезд 16 - 30, 3 подъезд 31 - 45, 4 подъезд 46 - 60
all_flat_in_entrance = numbers_apartment_at_floor * floors

# если есть остаток от деления номера квартиры на всего квартир на этаже
# мы берем полное количество подъездов и плюсуем 1 наш подъезд
if apartment % all_flat_in_entrance:
    entrance = apartment // all_flat_in_entrance + 1  # 59 // 15 = 3 + 1 = 4
else:  # а это как раз граничное значение последняя квартира на этаже 60 // 15 = 4 остатка от деления нет!
    entrance = apartment // all_flat_in_entrance

# здесь считаем номер в подъезде нашей квартиры от последней
number_apartment_in_entrance = all_flat_in_entrance * entrance - apartment

# квартира 46 (14 от последней 15 - 1) целочисленное деление даст нам 4
# квартира 47 (13 от последней 15 - 2) целочисленное деление даст нам 4
# квартира 48 (12 от последней 15 - 3) целочисленное деление даст нам 4
# а квартира 49 (11 от последней 15 - 4) целочисленное деление даст нам уже 3
# а квартира 59 (1 от последней 15 - 4) целочисленное деление даст нам уже 0
# и вычитая их из 5 количество этажей мы получим этажность
x = floors - number_apartment_in_entrance // numbers_apartment_at_floor

print(f'Номер квартиры - {apartment}, подъезд - {entrance}, этаж - {x}')

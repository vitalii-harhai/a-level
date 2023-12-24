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

all_flat_in_entrance = numbers_apartment_at_floor * floors

if apartment % all_flat_in_entrance:
    entrance = apartment // all_flat_in_entrance + 1
else:  # а это как раз граничное значение последняя квартира на этаже 60 // 15 = 4 остатка от деления нет!
    entrance = apartment // all_flat_in_entrance

number_apartment_in_entrance = all_flat_in_entrance * entrance - apartment

x = floors - number_apartment_in_entrance // numbers_apartment_at_floor

print(f'Номер квартиры - {apartment}, подъезд - {entrance}, этаж - {x}')
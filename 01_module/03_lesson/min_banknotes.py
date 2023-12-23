# declaration constants
BANKNOTES = (10, 20, 50, 100, 200, 500, 1000)
BANKNOTE_MAXIMUM = 10


# обраховуємо залишок невиданої суми
def calculate_balance(amount: int, banknote_distribution: dict) -> int:
    """
    Считаем остаток невыданной суммы
    :param amount: сумма к выдаче банкоматом
    :param banknote_distribution: словарь {номинал банкноты: количество банкнот}
    :return: обновленный словарь {номинал банкноты: количество банкнот}
    """
    balance_sum = amount
    for k, v in banknote_distribution.items():
        balance_sum -= k * v
    return balance_sum


def calculate_min_banknotes(amount: int) -> dict:
    item = 0
    amount_to_payment = dict()
    balance = amount

    while balance != 0:  # выходим когда остаток невыданной суммы равен 0
        banknote: int = BANKNOTES[item]  # берем банкноту из константы банкнот (от мелкой к крупной)
        balance = calculate_balance(amount, amount_to_payment)  # просчитали остаток невыданной суммы
        quantity = balance // banknote
        if balance > 0:  # если невыданная сумма больше 0 идем к большей банкноте
            if quantity >= BANKNOTE_MAXIMUM:  # если больше чем 10 количество принимаем 10
                quantity = 10
                amount_to_payment.update({banknote: quantity})  # обновили словарь банкнот и их количества
                item += 1  # и пошли к следующей более крупной банкноте
            if quantity < 10:  # значит банкнота последняя, ее берем на одну больше и остаток уходит в минус (значит больше дали)
                if balance != amount:
                    quantity += 1
                amount_to_payment.update({banknote: quantity})
                item -= 1  # и пошли к более мелкой назад
        elif balance < 0:  # больше дали чем надо, значит минусовый остаток переводим в + и считаем количество банкнот
            quantity = abs(balance) // banknote
            value = amount_to_payment[banknote]
            amount_to_payment.update({banknote: value - quantity})  # обновили словарь этой банкноты с уже меньшим количеством
            item -= 1  # и поехали к более мелкой банкноте

    return amount_to_payment


give_me_money = int(input(f'Enter the money like integer and multiple {BANKNOTES[0]}: '))

for b, q in calculate_min_banknotes(give_me_money).items():
    print(f'banknote = {b}, quantity = {q}')

# TEST
# def test_sum(test_dict: dict) -> int:
#     current_sum = 0
#     for x, y in test_dict.items():
#         current_sum += x * y
#     return current_sum
#
#
# error = ''
# for i in range(0, 10000, 10):
#     print(f'{i=}, {calculate_banknotes(i)=}, {i == test_sum(calculate_banknotes(i))=}')
#     if i != test_sum(calculate_banknotes(i)):
#         error += f'error in {i}'
# print(error)

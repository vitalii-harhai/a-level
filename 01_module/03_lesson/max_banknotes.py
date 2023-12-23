# declaration constants
BANKNOTES = (1000, 500, 200, 100, 50, 20, 10)


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


def calculate_max_banknotes(amount: int) -> dict:
    item = 0
    amount_to_payment = dict()
    balance = amount

    while balance != 0:  # выходим когда невыданная сумма будет 0
        banknote: int = BANKNOTES[item]  # берем банкноту из константы банкнот (с большей к нижней)
        balance = calculate_balance(amount, amount_to_payment)  # просчитали остаток невыданной суммы
        if balance // banknote >= 1:  # если остаток суммы можно выдать больше чем одной банкнотой
            quantity = balance // banknote
            amount_to_payment.update({banknote: quantity})  # обновили словарь банкнот и их количества
        if not banknote == BANKNOTES[-1]:  # и если это не последняя самая мелкая банкнота, пошли к следующей
            item += 1
    return amount_to_payment


give_me_money = int(input(f'Enter the money like integer and multiple {BANKNOTES[-1]}: '))

for b, q in calculate_max_banknotes(give_me_money).items():
    print(f'banknote = {b}, quantity = {q}')

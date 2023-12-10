#!/usr/bin/env python
# -*- coding: utf-8 -*-

def draw_line(characters=45):
    """
    Drawing horizontal line in console
    :param characters: quantity of simbols '-' to print
    :return: console output the specific character '-'
    """
    print('-' * characters)


if __name__ == '__main__':

    # declaration of the distribution value constant
    INCOME_DISTRIBUTION = {
        'Necessity Envelop': 0.55,  # NEC, необхідні витрати
        'Freedom Envelop': 0.1,  # FFA, фінансова свобода
        'Education Envelop': 0.1,  # EDU, освіта
        'Long Term Envelop': 0.1,  # LTSS, резерв та на великі покупки
        'Play Envelop': 0.1,  # PLAY, розваги
        'Give Envelop': 0.05  # GIVE, подарунки
    }

    # declaration of the expected income
    expected_income = 1000

    # greetings
    invite_message = 'Hello.\n' 'We gonna fill your envelops by the money you input here!\n' \
                     'Please input your amounts of money income and see the results.\n' 'Press Ctrl+C to exit script.\n'
    print(invite_message)
    draw_line()

    # declaration of the dictionary for saving current values
    user_income_distribution = dict()

    # initializing the handler for user input
    amount = 0

    while amount < expected_income:

        current_amount = input('Enter the amount please (like integer number): ')
        if current_amount.isdigit():
            amount += int(current_amount)
        else:
            print('Enter the integer number!')

    # calculate the distribution
    for key in INCOME_DISTRIBUTION:
        current_value = INCOME_DISTRIBUTION[key] * amount
        user_income_distribution.update({key: current_value})

    # print final distribution table
    print('\nAt the end we have:')
    draw_line()
    print(f'|{"Expense item":^32}|{"Amount":^10}|')
    draw_line()
    for key, value in user_income_distribution.items():
        print(f'| {key:<31}|{value:^10.0f}|')
    draw_line()
    print(f'| {"Total":<31}|{amount:^10.0f}|')
    draw_line()
    print(f'Thanks for using our software \N{GRINNING FACE}')

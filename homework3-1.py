# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def my_division(dividend=float(input('Enter the dividend value: '))
                , divider=float(input('Enter the divider value: '))):
    """Returns result of dividing two numbers"""
    while divider == 0:
        try:
            divider != 0
            return dividend / divider
        except ZeroDivisionError:
            print('Error! '
                  'The divisor value cannot be equal to zero')
            divider = float(input('Enter the divider value: '))
    return dividend / divider


print(my_division())

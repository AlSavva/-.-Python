# Программа принимает действительное положительное число x и целое
# отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y). При
# решении задания необходимо обойтись без встроенной функции возведения числа
# в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в
# степень с помощью оператора **. Второй — более сложная реализация без
# оператора **, предусматривающая использование цикла.

def my_pow(x, y):
    """Function implementing the operation of raising to a negative exponent

    This function takes a real positive number and a negative integer
    as arguments.

    x: float, y: int, and y < 0
    """
    if int(y) >= 0:
        return 'Error! y argument cannot be greater than zero'
    try:
        x != 0
        return 1 / x ** -y
    except ZeroDivisionError:
        return 'Error! x argument cannot be zero'

# Вариант без использования встроенной функции возведения в степень

def my_2pow(x, y):
    """Function implementing the operation of raising to a negative exponent,
    but does not use the exponentiation operation

    This function takes a real positive number and a negative integer
    as arguments.

    x: float, y: int, and y < 0
    """
    if int(y) >= 0:
        return 'Error! y argument cannot be greater than zero'
    try:
        x != 0
        res = 1
        count = 0
        while count != -y:
            count += 1
            res *= 1 / x
        return res
    except ZeroDivisionError:
        return 'Error! x argument cannot be zero'


print(my_pow(2, -2))
print(my_2pow(2, -2))

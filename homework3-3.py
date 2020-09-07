# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    """The function accepts three positional arguments, int or float,
and returns the sum of the largest two arguments."""
    return (a + b + c) - min(a, b, c)


print(my_func(-5, -7, -6))

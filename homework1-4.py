# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения
# используйте цикл while и арифметические операции.

number = int(input())
num_max = number % 10
while number > 0:
    if number % 10 > num_max:
        num_max = number % 10
    number //= 10
print(num_max)

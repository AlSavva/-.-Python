# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните
# в переменные, выведите на экран.

name = input('Привет, введите своё имя:')
while True:
    number = int(input(f'{name},'
                       f' введите число больше 0'
                       f' и меньше 10 и я возведу его в куб:'))
    if 0 < number < 10:
        print(f'{name}, {number} в кубе равно: {number ** 3}')
        break
    else:
        print('Ошибка! Число должно быть меньше 10 и больше 0!')
print('Конец!')
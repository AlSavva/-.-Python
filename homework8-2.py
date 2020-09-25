# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на
# нуль. Проверьте его работу на данных, вводимых пользователем. При вводе
# пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyZerroDivErr(Exception):
    def __init__(self, text):
        self.text = text


dividend = float(input('Input dividend: '))
divider = float(input('Input divider: '))
try:
    if divider == 0:
        raise MyZerroDivErr('Attention! Division by zero!')
    print(dividend / divider)
except MyZerroDivErr as err:
    print(err)

# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.
import sys

try:
    name, work_time, hour_rate, bonus = sys.argv
    try:
        work_time, hour_rate, bonus = int(work_time), float(
            hour_rate), float(
            bonus)
        print(f'Выработка в часах: {work_time}\nСтавка в час: {hour_rate:.2f}'
              f'\nПремия: {bonus:.2f}')
        print(f'Зарплата: {(work_time / hour_rate) + bonus:.2f}')
    except ValueError:
        print('Ошибка! Введите числовые значения!')
except ValueError:
    if len(sys.argv) < 4:
        print('Ошибка! Недостаточно аргументов!')
    else:
        print('Ошибка! Слишком много аргументов!')

# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.

#  Вариант №1 ввод данных пользователем

try:
    with open('text_result_5.txt', 'w', encoding='utf-8') as out_file:
        chek = None
        total = 0
        while chek != 'q':
            my_list = list(map(int, input('Enter numbers separated by spaces: '
                                          '').split()))
            out_file.write(' '.join([str(num) for num in my_list]) + '\n')
            total += sum(my_list)
            print(f'Sum of numbers in a row: {sum(my_list)}\n'
                  f'Sum of numbers in a file: {total}')
            out_file.seek(0, 2)
            chek = input('any key to continue, "q" to exit: ')
except ValueError as Error:
    print('Error!Only numbers!')
except IOError:
    print('IOError')


# Вариант №2 с вводом данных из генерируемых списков

def gen_list(begin=0, end=100, len_l=10):
    """Функция генерирует список длинны len_l из случайных целых чисел из
    диапазона begin-end"""
    from random import randint
    lst = []
    for i in range(len_l):
        lst.append(randint(begin, end))
    return lst


try:
    with open('text_result_5.txt', 'w+', encoding='utf-8') as out_file:
        chek = None
        total = 0
        while chek != 'q':
            my_list = gen_list(1, 7, 10)
            out_file.write(' '.join([str(num) for num in my_list]) + '\n')
            out_file.seek(0)
            for line in out_file:
                new_list = list(map(int, line.split()))
                total += sum(new_list)
            print(f'Sum of numbers in a row: {sum(my_list)}\n'
                  f'Sum of numbers in a file: {total}')
            out_file.seek(0, 1)
            total = 0
            chek = input('any key to continue, "q" to exit: ')
except ValueError as Error:
    print('Error')
except IOError:
    print('IOError')

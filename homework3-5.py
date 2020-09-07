# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа
# вводится специальный символ, выполнение программы завершается. Если
# специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def sum_mylist():
    """The function requests gets a string of numbers separated by a space.
    When you press Enter, it returns the sum of the numbers. You can continue
    entering numbers separated by a space and press Enter again. The sum of
    the newly entered numbers will be added to the amount already calculated.
    But if 'Q' is entered instead of a number, the function is terminated."""
    res = 0
    while True:
        numbers = input('Enter a string of numbers separated by a space. '
                        '\nTo exit, enter "q": ').split()
        for number in numbers:
            try:
                number.isdigit()
                res += float(number)
            except:
                if number.upper() == 'Q':
                    return print(f'The programme is completed! '
                                 f'Sum of entered numbers: {res}')
                else:
                    return print('Input error! Program terminated!')
        print(f'Sum of entered numbers: {res}')


sum_mylist()

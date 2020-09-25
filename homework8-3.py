# Создайте собственный класс-исключение, который должен проверять содержимое
# списка на наличие только чисел. Проверить работу исключения на реальном
# примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class MyNotDigitErr(Exception):
    def __init__(self, txt):
        self.txt = txt


chek = None
my_list1 = []
while chek != 'q':
    my_list = list(input('Enter numbers separated by spaces: ').split())
    for el in my_list:
        try:
            if el.isdigit():
                my_list1.append(int(el))
            elif len(el.split('.')) == 2 and (el.split('.')[0].isdigit() and
                                              el.split('.')[1].isdigit()):
                my_list1.append(float(el))
            else:
                raise MyNotDigitErr(
                    f'Error!You entered "{el}". Only a number can be added to '
                    f'the list.')
        except MyNotDigitErr as err:
            print(err)
    print(my_list1)
    chek = input('Enter, or any key+Enter to continue, "q" to exit: ')
print('The end!')

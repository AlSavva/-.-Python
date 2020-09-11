# Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных свидетельствует
# пустая строка.
try:
    with open('text_1.txt', 'w', encoding='utf-8') as my_outfile:
        my_line = input('enter anything:\n')
        while my_line:
            my_outfile.writelines(my_line + '\n')
            my_line = input()
    with open('text_1.txt', 'r', encoding='utf-8') as my_outfile:
        print(my_outfile.read())
except IOError:
    print('IOError')

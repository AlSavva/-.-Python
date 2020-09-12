# Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников имеет
# оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.
try:
    with open('text_3.txt', 'r', encoding='utf-8') as my_infile:
        in_file_list=my_infile.readlines()
        print('List of employees with a salary of less than 20,000: ')
        print(*[line.split()[0] for line in in_file_list if float
        (line.split()[1]) < 20000], sep='\n')
        my_infile.seek(0)
        print(f'Average employee salary: '
              f'{sum([float(line.split()[1]) for line in in_file_list])/len(in_file_list):.2f}')
except IOError:
    print('IOError')
except IndexError:
    print('IndexError.Invalid data in the source file')
except ValueError:
    print('ValueError.Enter a number')

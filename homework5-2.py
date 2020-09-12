# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
try:
    with open('text_2.txt', 'r+', encoding='utf-8') as my_infile:
        if len(my_infile.read()) == 0:  # check if the text is in the file
            my_line = input('enter anything:\n')
            while my_line:
                my_infile.writelines(my_line + '\n')
                my_line = input()
        my_infile.seek(0)  # "carriage return"
        print(f'File "text_2.txt" contain {len(my_infile.readlines())} lines '
              f'of text.')
        my_infile.seek(0)  # "carriage return"
        for n, l in enumerate(my_infile.readlines()):
            print(f'String #{n + 1}: '
                  f'{(f"{len(l.split())} words." if len(l.split()) != 0 else "empty.")}')
except IOError:
    print('IOError')

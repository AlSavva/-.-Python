# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на
# русские. Новый блок строк должен записываться в новый текстовый файл.
from googletrans import Translator

trans = Translator()
try:
    with open('text_4.txt', 'r', encoding='utf-8') as in_file:
        with open('text_result_4.txt', 'w', encoding='utf-8') as out_file:
            print(*[trans.translate(line, dest='ru').text for
                    line in in_file], sep='\n')
            in_file.seek(0)
            out_file.writelines('\n'.join([trans.translate(
                line, dest='ru').text for line in in_file]))
except IOError:
    print('IOError')

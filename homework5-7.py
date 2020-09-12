# Создать (не программно) текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней
# прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их
# прибылями, а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

try:
    with open('text_7.txt', 'r', encoding='utf-8') as infile:
        first_dict = {}
        second_dict = {}
        sum_res = 0
        bad_res = 0
        for line in infile:
            if int(line.split()[2]) - int(line.split()[3]) >= 0:
                sum_res += int(line.split()[2]) - int(line.split()[3])
            else:
                bad_res += 1
            sum_res += int(line.split()[2]) - int(line.split()[3])
            first_dict[line.split()[0]] = int(line.split()[2]) - int(
                line.split()[3])
        infile.seek(0)
        second_dict['average_profit'] = sum_res / (
                    len(infile.readlines()) - bad_res)
    with open('text_77.json', 'w', encoding='utf-8') as outfile:
        json.dump([first_dict, second_dict], outfile, ensure_ascii=False)
except IOError:
    print('IOError')

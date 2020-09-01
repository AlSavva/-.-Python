# Реализовать структуру данных «Товары». Она должна представлять собой список
# кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже
# должно быть два элемента — номер товара и словарь с параметрами (характеристиками
# товара: название, цена, количество, единица измерения). Структуру нужно
# сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый
# ключ — характеристика товара, например название, а значение — список значений
# -характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
# Код получился длинным из-за соблюдения POP-8б и создания подобия интерфейса,
# с проверкой вводимых данных.

product_list = ['Computer', 'Printer', 'Scanner', 'Cheeseburger']
print('В базе есть следующие наименования товаров:', ', '.join(product_list))
user_add = input('Если в списке нет нужного вам наименования, \nвведите его '
                 'самостоятельно. Для отказа, введите любую цифру:')
while not user_add.isdigit():
    product_list.append(user_add.title())
    print('В базе есть следующие наименования товаров:',
          ', '.join(product_list))
    user_add = input('При необходимости введите еще товар, или введите любую '
                     'цифру чтобы продолжить: ')
    for name in product_list:
        if user_add == name:
            user_add = input(f'Ошибка! {user_add}'
                             f' уже есть в списке наименований! '
                             f'Ведите другое наименование, или введите '
                             f'любую цифру, чтобы продолжить: ')
prod_quant = int(input('Выберите количество наименований для внесения в '
                       'аналитическую базу: '))
pre_count = prod_quant
count = 0
base_list = []
while prod_quant > 0:
    select_list = []
    select_dict = {}
    count += 1
    print(f'Выберите продукт {count} из {pre_count}')
    for index, item in enumerate(product_list):
        print(str(index + 1) + '.', item)
    user_select = int(input(f'Введире цифры из диапазона '
                            f'1-{len(product_list)}: '))
    while user_select not in range(1, len(product_list) + 1):
        user_select = int(input(f'Ошибка! Введире цифры из диапазона '
                                f'1-{len(product_list)}: '))
    for i in range(len(base_list)):
        if user_select == base_list[i][0]:
            user_select = int(
                input(f'Ошибка! {product_list[user_select - 1].title()}'
                      f' уже есть в аналитической базе! '
                      f'Выберите другой продукт: '))
    print(f'Вы выбрали {product_list[user_select - 1].lower()}')
    select_list.append(user_select)
    select_dict['Product'] = product_list[user_select - 1]
    user_price = float(
        input(f'Для товара {product_list[user_select - 1].lower()} '
              f'введите стоимость: '))
    select_dict['Price'] = user_price
    user_quant = int(input(f'Введите количество для товара '
                           f'{product_list[user_select - 1].lower()}: '))
    select_dict['Quantity'] = user_quant
    user_unit = input('Введите единицу измерения: ')
    select_dict['Unit of measurement'] = user_unit
    select_list.append(select_dict)
    base_list.append(tuple(select_list))
    prod_quant -= 1
base_dict = {}
for i in range(len(base_list)):
    for key, value in base_list[i][1].items():
        if key not in base_dict:
            base_dict[key] = []
        base_dict[key].append(value)
print('Аналитическая база по введенным вами данным сформирована:')
for key, value in base_dict.items():
    print(key + ': ', value)

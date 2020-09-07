# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать
# вывод данных о пользователе одной строкой.

def my_dossier(name='', surname='', year='', city='', email='',
               phone=''):
    """The function accepts several parameters that describe the user's data:
        first name, last name, year of birth, city of residence, email, phone
        number as named arguments. If no arguments are entered, the function
        will request their value from the user. The function outputs data in a
        single line."""

    if name == '':
        name = input('Enter name: ')
    if surname == '':
        surname = input('Enter surname: ')
    if year == '':
        year = input('Enter birth year: ')
    if city == '':
        city = input('Enter city: ')
    if email == '':
        email = input('Enter email: ')
    if phone == '':
        phone = input('Enter phone number: ')
    print(*[name, surname, year, city, email, phone])


# Вариант №2

def my_dossier2():
    any_tuple = ('name', 'surname', 'year of birth', 'place of residence',
                 'email', 'phone')
    any_dict = {}
    for el in any_tuple:
        any_dict[el] = input(f'Enter your {el}: ')
    print(', '.join(
        [': '.join((key, items)) for key, items in any_dict.items()]))


my_dossier()
my_dossier2()

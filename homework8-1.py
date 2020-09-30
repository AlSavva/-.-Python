# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два
# метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например,
# месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.
class MyData:
    def __init__(self, dmy=input('Enter data in format dd-mm-yyyy: ')):
        self.day, self.month, self.year = map(int,
                                              MyData.datavalid(dmy).split('-'))

    @staticmethod
    def datavalid(strdat):
        my = list(map(int, strdat.split('-')))
        if my[2] >= 10000:
            print(f'Invalid year in {strdat}. Replaced by 9999')
            my[2] = 9999
        if my[1] <= 0:
            print(f'Invalid month in {strdat}. Replaced by 1')
            my[1] = 1
        elif my[1] > 12:
            print(f'Invalid month in {strdat}. Replaced by 12')
            my[1] = 12
        if my[0] <= 0:
            print(f'Invalid day in {strdat}. Replaced by 01')
            my[0] = 1
        elif my[0] > 30 and my[0] in [4, 6, 9, 11]:
            print(f'Invalid day in {strdat}. Replaced by 30')
            my[0] = 30
        elif my[0] > 31 and my[1] in [1, 3, 5, 7, 8, 10, 12]:
            print(f'Invalid day in {strdat}. Replaced by 31')
            my[0] = 31
        if my[0] > 28 and my[1] == 2:
            if my[2] % 4 == 0 and my[2] % 100 != 0 or my[2] % 400 == 0:
                print(f'Invalid day in {strdat}. Replaced by 29')
                my[0] = 29
            else:
                print(f'Invalid day in {strdat}. Replaced by 28')
                my[0] = 28
        return f'{my[0]:02}-{my[1]:02}-{my[2]:04}'

    @classmethod
    def dataform(cls, strdata):
        return list(map(int, MyData.datavalid(strdata).split('-')))


a = MyData()
print(a.day, a.month, a.year)
print(type(a))
print(MyData.dataform('36-11-2012'))
a = MyData.datavalid('31-02-1965')
print(MyData.dataform(a))
print(MyData.datavalid('12-12-2020'))

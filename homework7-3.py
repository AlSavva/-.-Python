# Реализовать программу работы с органическими клетками. Необходимо создать
# класс Клетка. В его конструкторе инициализировать параметр, соответствующий
# количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание
# (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы
# должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В
# методе деления должно осуществляться округление значения до целого числа.
class Cell:
    def __init__(self, size: int):
        assert size >= 0, 'Only a positive integer!'
        self.size = size

    def __add__(self, other):
        return Cell(self.size + other.size)

    def __sub__(self, other):
        if (self.size - other.size) < 0:
            print(f'subtraction is not possible! the cell that is being '
                  f'\nreduced is smaller than the cell that is being '
                  f'subtracted')
            return Cell(0)
        else:
            return Cell(self.size - other.size)

    def __mul__(self, other):
        return Cell(self.size * other.size)

    __rmul__ = __mul__

    def __floordiv__(self, other):
        try:
            return Cell(self.size // other.size)
        except ZeroDivisionError:
            print('ZeroDivisionError')

    def make_order(self, cols: int):
        try:
            for i in range(self.size // int(cols)):
                print("*" * cols)
            print("*" * (self.size % cols))
        except ZeroDivisionError:
            print('ZeroDivisionError')
        except TypeError:
            print(f'TypeError! Only integer.')


a = Cell(28)
b = Cell(31)
print(a.size)
print(b.size)
print((b - a).size)
c = b - a
print(type(c), c.size)
print((a * b).size)
print((b * a).size)
print((a // b).size)
print((b // a).size)
a.make_order(5)

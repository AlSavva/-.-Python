# Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число», реализуйте перегрузку методов сложения и умножения
# комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class MyComplex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.real}{self.imaginary}i' if \
            self.imaginary <= 0 else f'{self.real}+{abs(self.imaginary)}i'

    def __add__(self, other):
        return MyComplex(self.real + other.real,
                         self.imaginary + other.imaginary)

    def __mul__(self, other):
        if isinstance(other, MyComplex):
            return MyComplex(
                self.real * other.real - self.imaginary * other.imaginary,
                self.real * other.imaginary + other.real * self.imaginary)
        elif isinstance(other, int) or isinstance(other, float):
            return MyComplex(self.real * other, self.imaginary * other)
        else:
            return 'Error! Only MyComplex, int, or float!'

    __rmul__ = __mul__


m = MyComplex(2, -3)
print(m)
b = MyComplex(3, 4)
print(b)
print(m + b)
print(m * b)
print(b * m)

# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом сложения
# должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix: list):
        lens = []
        lens += [len(matrix[i]) for i in range(len(matrix))]
        if len(set(lens)) == 1:
            self.matrix = matrix
        else:
            for i in range(len(matrix)):
                while len(matrix[i]) < max(lens):
                    matrix[i].append(0)
            self.matrix = matrix
            print(f'All rows in the matrix must have the same size. \nMissing '
                  f'values were replaced with zeros.\n{Matrix(matrix)}')

    def __str__(self):
        return '\n'.join(
            ['\t'.join([str(el[i]) for i in range(len(el))]) for el in
             self.matrix])

    @property
    def size(self):
        matrix_rows = len(self.matrix)
        matrix_cols = 0
        for row in self.matrix:
            if len(row) > matrix_cols:
                matrix_cols = len(row)
        return matrix_rows, matrix_cols

    def __add__(self, other):
        if self.size != other.size:
            return f'Different sizes!!! Addition is not possible.\n' \
                   f'{Matrix(self.matrix)}\n\n{Matrix(other.matrix)}'

        else:
            new_matrix = []
            for i in range(len(self.matrix)):
                temp = []
                for j in range(len(self.matrix[i])):
                    temp.append(self.matrix[i][j] + other.matrix[i][j])
                new_matrix.append(temp)
            return Matrix(new_matrix)


my = Matrix([[1, 3, 5], [6, 2, 7], [1, 2, 9]])
print(my)
print()
my2 = Matrix([[1, 13, 3], [6, 2, 16, 4], [1, 2, 83]])
sd = [[1, 2, 3, 6], [9, 9, 6, 6], [5, 8, 8, 6]]
print()
sd_matr = Matrix(sd)
print()
print(sd_matr)
print()
print(my2)
print()
print(sd_matr + my2)
print()
print(my.size, my2.size, sd_matr.size)
print()
print(my2 + my)

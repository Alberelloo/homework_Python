# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, list):
        self.list = list

    def str(self):
        print('Matrix')
        for row in self.list:
            print(row)

    def __add__(self, other):
        matrix = []
        for i in range(len(self.list )):
            row = []
            for j in range(len(self.list[i])):
                a = self.list[i][j] + other.list[i][j]
                row.append(a)
            matrix.append(row)

        for row in matrix:
            print(row)

mat_1 = Matrix([[2, 5, 1], [3, 7, 0], [4, 9, 8]])
mat_1.str()

print( )

mat_2 = Matrix([[7, 1, 8], [6, 9, 0], [3, 2, 5]])
mat_2.str()

print( )

print(mat_1 + mat_2)
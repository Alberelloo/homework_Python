# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его конструкторе инициализировать
# параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов.
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление
# клеток, соответственно.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда
# не хватает, то в последний ряд записываются все оставшиеся.

class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num >= other.num:
            return Cell(self.num - other.num)
        else:
            print('Невозможное вычитание')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, count):
        ord = ''
        for i in range(self.num // count ):
            ord += '*' * count + '\n'
        ord += '*' * (self.num % count) + '\n'
        return ord

    def __str__(self):
        return f'{self.num}'

cell_1 = Cell(55)
print(cell_1.make_order(11))

cell_2 = Cell(5)
print(cell_2.make_order(3))

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2 - cell_1)
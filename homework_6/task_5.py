# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»; создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):
    def draw(self):
        print('Рисуем ручкой')

class Pencil(Stationary):
    def draw(self):
        print('Рисуем карандашом')
class Handle(Stationary):
    def draw(self):
        print('Рисуем маркером')

my_pen = Pen('pen')
my_pencil = Pencil('pencil')
my_handle = Handle('handle')

for i in (my_pen, my_pencil, my_handle):
    i.draw()
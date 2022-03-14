# 2. Реализовать класс Road (дорога). Определить атрибуты: length (длина), width (ширина); значения атрибутов должны
# передаваться при создании экземпляра класса; атрибуты сделать защищёнными; определить метод расчёта массы асфальта,
# необходимого для покрытия всей дороги; использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна; проверить работу метода.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count(self, mass, thickness):
        self.mass = mass
        self.thickness = thickness
        count = self._length * self._width * mass * thickness / 1000
        print(count)
road = Road(20, 5000)

road.count(25,5)

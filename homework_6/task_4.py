# 4. Реализуйте базовый класс Car. у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также
# методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда); опишите
# несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar; добавьте в базовый класс метод show_speed, который должен
# показывать текущую скорость автомобиля; для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости. Создайте экземпляры классов, передайте
# значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости')

class PoliceCar(Car):
    pass
my_car_1 = TownCar(50, 'зеленый', 'моя машина')
my_car_2 = SportCar(207, 'зеленый', 'гоночная машина')
my_car_3 = WorkCar(60, 'зеленый', 'рабочая машина')
my_car_4 = PoliceCar(50, 'зеленый', 'полицейская машина', True)

my_car_1.show_speed()
my_car_3.show_speed()

my_car_3.speed = 20
my_car_3.show_speed()

my_car_1.turn('направо')

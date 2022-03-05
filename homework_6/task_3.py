# 3. Реализовать базовый класс Worker (работник). определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker; в классе Position реализовать методы получения полного имени
# (get_full_name) и дохода с учётом премии (get_total_income); проверить работу примера на реальных данных: создать экземпляры
# класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'оклад': wage, 'премия': bonus}

class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(self._income['оклад'] + self._income['премия'])

employee_1 = Position('Александр', 'Алехин', 'санитар', 30000, 50000)


employee_1 .get_full_name()
employee_1 .get_total_income()
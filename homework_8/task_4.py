# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для
# классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры,
# общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
# Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.


class Storage:

    def __init__(self, equipment):
        self.equipment = {}

    def get_supply(self, equipment):
        for key, value in equipment.items():
            if key in self.equipment:
                self.equipment[key] += value
            else:
                self.equipment = value

    def give_equipment(self, department, equipment):
        if equipment.id in self.equipment and self.equipment[equipment.id] > 0:
            self.equipment[equipment.id] -= 1

    def get_equipment(self, department, equipment):
        if department.return_equipment(equipment):
            equip.dict = {equipment.id: 1}
            self.get_supply(equip.dict)


class Office_Equipment:
    def __init__(self, type: str, model: str, cost: float, sn: str):
        self.type = str(type)
        self.model = str(model)
        self.cost = float(cost)
        self.sn = str(sn)

    def __str__(self):
        return f"{self.type} {self.model}"

class Printer(Office_Equipment):
    cur_id = 1
    def __init__(self, model: str, cost: float, is_colorful: bool, sn: str, id):
        self.is_colorful = is_colorful
        super().__init__('Принтер', model, cost, sn)
        self.id = id
        cur_id= self.id
        cur_id += 1

class Scanner(Office_Equipment):
    cur_id = 1
    def __init__(self, model: str, cost: float, dpi: str, sn: str, id):
        self.dpi = dpi
        super().__init__('Сканер', model, cost, sn)
        self.id = id
        cur_id = self.id
        cur_id += 1

class Xerox(Office_Equipment):
    cur_id = 1
    def __init__(self, model: str, cost: float, is_colorful: bool, dpi: str, velocity: int, sn: str, id):
        self.is_colorful = is_colorful
        self.dpi = dpi
        self.velocity = velocity
        super().__init__('Ксерокс', model, cost, sn)
        self.id = id
        cur_id = self.id
        cur_id += 1

class Department:
    def __init__(self, name):
        self.name = name
        self.equipment = []

    def get_equipment(self, equipment):
        self.equipment.append(equipment)
        print(f'{self.name} - {self.equipment}')

    def return_equipment(self, equipment):
        if equipment in self.equipment:
            self.equipment.remove(equipment)
            print(f'{self.name} - {self.equipment}' )






printer_1 = Printer('Epson L120', 7300.12, True, 'N6SS549876548', 8)
printer_2 = Printer('HP Laser 107a', 6600, False, 'FG64855SFG5', 2)
scanner_1 = Scanner('Epson Perf V19', 5010, '4800x4800', '65482321FF5', 0)
scanner_2 = Scanner('Canon LiDE 300', 4700.45, '2400x2400', '31313131FFF', 1)
xerox_1 = Xerox('Canon PIXMA MG2540S', 2299.73, True, '4800x600', 8, 'FG8#HHHF', 3)
xerox_2 = Xerox('HP LaserJet M132nw', 14604.20, False, '1200x1200', 22, '9BB654848554', 13)
equipment = {printer_1, printer_2, scanner_1, scanner_2, xerox_1 , xerox_2}
dep_1 = Department('PR')
dep_2 = Department('R&D')
storage = Storage(equipment)

dep_1.get_equipment(printer_2)
dep_1.get_equipment(printer_2)
dep_1.get_equipment(printer_2)
dep_1.get_equipment(printer_2)
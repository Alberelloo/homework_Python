# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений
# необходимо запускать скрипт с параметрами.

from sys import argv

wage = float(argv[1])
hours = float(argv[2])
premium = float(argv[3])

payment = (wage * hours) + premium
print(f'Зарплата - {payment}')

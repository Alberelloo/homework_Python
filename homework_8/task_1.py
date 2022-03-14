# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса
# реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу
# полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def method_1(cls, date):
        my_date = []

        for i in date.split('-'):
            my_date.append(i)
        return f'{int(my_date[0])} {int(my_date[1])} {int(my_date[2])}'

    @staticmethod
    def method_2(date):
        my_date = []

        for i in date.split('-'):
            my_date.append(i)

        if (int(my_date[0]) > 31) or (int(my_date[0]) < 0):
            if (int(my_date[1]) > 12) or (int(my_date[1]) < 0):
                if (int(my_date[2]) < 0):
                    print('Year is out of range')
                print('Month out of range')
            print('Day out of range')
        else:
            print('All right')

print(Date.method_1('10 - 03 - 2022'))
print(Date.method_2('32 - 03 - 2022'))
print(Date.method_2('10 - 03 - 2022'))

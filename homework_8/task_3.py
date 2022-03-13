# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения
# на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами. Класс-исключение должен
# контролировать типы данных элементов списка.

class Digit(Exception):
    def __init__(self, text):
        self.text = text

new_list = []

while True:
    data = input('Введите елемент: ')
    if data == 'stop':
        break
    else:
        try:
            try:
                new_list.append(int(data))
                print(new_list)
            except ValueError:
               raise Digit(' ')
        except Digit:
            pass


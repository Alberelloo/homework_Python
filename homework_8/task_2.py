# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionZero(Exception):
    def __init__(self, text):
        self.text = text


dividend = int(input('Введите делимое: '))
divisor = int(input('Введите делитель: '))

try:
    if divisor == 0:
        raise DivisionZero('Деление на 0')
except DivisionZero:
    print('Деление на 0 запрещено')
else:
    print(dividend/ divisor)





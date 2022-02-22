# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.
dividend = float(input('Введите делимое: '))
divisor = float(input('Введите делитель: '))

def div(dividend, divisor):
    try:
        dividend / divisor == 0
    except:
        print('Деление на 0')
    else:
        return(dividend / divisor)

print(div(dividend, divisor))

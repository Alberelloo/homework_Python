# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.

#1
from itertools import cycle, count
#
# for el in count(1):
#     if el < 27:
#         print(el)
#     else:
#         break

#2
list = list(map(int, input('Введите числа: ').split()))
for ind, el in enumerate(cycle(list)):
    if ind > 20:
        break
    else:
        print(el)
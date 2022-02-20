# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

list = [16, 9, 8, 4, 3, 3, 3, 1, 0]
elem = int(input('Введите число: '))

for i in list:
    if i < elem:
       index = list.index(i)
       list.insert(index, elem)
       break
    elif i == elem:
        list.reverse()
        index = list.index(i)
        list.insert(index, elem)
        list.reverse()
        break

print(list)

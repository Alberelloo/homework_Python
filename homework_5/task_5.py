# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
from random import randint
with open('text_5.txt', 'w') as file_obj:
    for i in range(41):
        file_obj.write(f'{randint(0,100)} ')

with open('text_5.txt') as f_obj:
    content = f_obj.read().split()
    content = list(map(int, content))
    summ = sum(content)
    print(summ)
    
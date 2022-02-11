# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input('Введите число:')
number_2 = int(number * 2)
number_3 = int(number * 3)
fin_number = int(number) + number_2 + number_3

print(fin_number)
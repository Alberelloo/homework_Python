# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и dict.

month = int(input('Введите месяц: '))

list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'fall', 'fall', 'fall', 'winter']
print(list[month - 1])

# year_dict = {1 : 'winter', 
#              2 : 'winter',
#              3 : 'spring',
#              4 : 'spring',
#              5 : 'spring',
#              6 : 'summer',
#              7 : 'summer',
#              8 : 'summer',
#              9 : 'fall',
#              10 : 'fall',
#              11 : 'fall',
#              12 : 'winter',
#             }
# print(year_dict[month])
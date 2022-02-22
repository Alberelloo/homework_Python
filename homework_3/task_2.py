# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.
def info(name, surname, year, city, email, phone):
    return(f'{name}, {surname}, {year}, {city}, {email}, {phone}')

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год: ')
city = input('Введите город: ')
email = input('Введите почту: ')
phone =input('Введите телефон: ')

result = info(name=name, surname=surname, year=year, city=city, email=email, phone=phone)
print(result)
# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину
# их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.

with open('text_3.txt', encoding="utf-8") as file_obj:
    content = file_obj.readlines()
    total_salary = []
    for line in content:
        space = line.rfind(' ')
        name = line[:space]
        salary = line[space:]
        total_salary.append(float(salary))
        if float(salary) < 20000:
            print(name)
av_salary = sum(total_salary) / len(total_salary)
print(f'Средняя з/п - {av_salary}')

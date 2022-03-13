# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать
# данные о фирме: название, форма собственности, выручка, издержки. Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также
# словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
import json
with open('text_7.txt', encoding = 'utf-8') as file_obj:
    content = file_obj.readlines()
    profit = []
    company = {}
    for line in content:
        line = line.split(' ')
        income = int(line[-2])
        costs =  int(line[-1])
        print(f'Прибыль {line[0]}: {income - costs}')
        if income > costs:
            profit.append(income - costs)
        av_profit = sum(profit) / len(profit)
        company.update({line[0]:income - costs})
    info = [company, {'Средняя прибыль': av_profit}]

with open('info.json', 'w', encoding = 'utf-8') as result:
    json.dump(info,result)

with open('info.json', encoding = 'utf-8') as result:
    result = json.load(result)
    print(result)

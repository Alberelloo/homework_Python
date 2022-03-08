# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий. Сформировать словарь, содержащий название
# предмета и общее количество занятий по нему. Вывести его на экран.

sched = {}

with open('text_6.txt', encoding = 'utf-8') as f_obj:
    content = f_obj.readlines()
    for line in content:
        line = line.replace(':','')
        line = line.replace('\n', '')
        line = line.split(' ')
        subj = str(line[:-3])
        hours = line[-3:]
        time = 0
        for elem in hours:
            try:
                elem = int(elem)
            except ValueError:
                elem = 0
            else:
                time += int(elem)
        sched.update({subj: time})
print(sched)






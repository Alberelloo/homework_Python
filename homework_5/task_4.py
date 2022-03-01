# Создать (не программно) текстовый файл со следующим содержимым. Напишите программу, открывающую
# файл на чтение и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
def span(n):
   for i in range(n):
        content = file_obj.readline()
        space = content.find(' ')
        name = content[:space]
        new_obj.writelines((content.replace(name, nums[i])))

with open('text_4_new.txt','w', encoding = 'utf-8') as new_obj:
    with open('text_4.txt', encoding = 'utf-8') as file_obj:
        nums =['Один', 'Два', 'Три', 'Четыре']
        span(4)

        # без readline()

        # for ind, line in enumerate(file_obj):
        #     space = line.find(' ')
        #     name = line[:space]
        #     new_obj.writelines((line.replace(name, nums[ind])))

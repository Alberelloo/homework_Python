# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('text_2.txt') as file_obj:
    str = 0
    content = file_obj.readlines()
    for ind, elem in enumerate(content):
        words = elem.split(' ')
        print(f'{ind + 1} строка, слов - {len(words)}')
        str += 1
print(f'всего {str} строк')
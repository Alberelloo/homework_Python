# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

user_input = input('')

def int_func(user_input):
    return user_input.title()
# print(int_func(user_input))

# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово состоит из латинских
# букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте написанную
# ранее функцию int_func().

def title(user_input):
    input = user_input.split()
    for i in input:
        return int_func(user_input)

print(title(user_input))
# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def summ(num_1,num_2,num_3):
    nums = [num_1,num_2,num_3]
    nums.sort()
    summ = nums[1] + nums[2]
    return(summ)

num_1 = int(input('Введите число: '))
num_2 = int(input('Введите число: '))
num_3 = int(input('Введите число: '))

summ = summ(num_1,num_2,num_3)
print(summ)

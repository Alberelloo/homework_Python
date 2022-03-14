import numpy as np
import math as m

#функция для проверки len(input) =? x^2
def isint(n):
    if n % 1 == 0:
        return True
    else:
        return False

# ввод данных и вычисление r/c
elem = input('Введите данные: ').split(' ')
elem = list(map(int, elem))
side = m.sqrt(len(elem))

# проверка квадратности матрицы
if not isint(side):
    raise Exception('Матрица не квадратная')

# задание матрицы
side = int(side)
matrix = [elem[i:i+side] for i in range(0,len(elem),side)]

print('Матрица:')
for i in matrix:
    print(f'{i}')

print()

# транспонирование матрицы
matrix_transp = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print('Транспонированная матрица:')
for r in matrix_transp:
   print(r)

print()

# -1 * транспонированную матрицу
matrix_transp_neg = []
for ind, i in enumerate(matrix_transp):
    for j in matrix_transp[ind]:
        matrix_transp_neg.append(-1 * j)

matrix_transp_neg = [matrix_transp_neg[i:i+side] for i in range(0,len(matrix_transp_neg),side)]

print('- Транспонированная матрица')
for r in matrix_transp_neg:
   print(r)

print()
# Проверка (анти)рефлексивности

refl = []

for i in range(side):
    refl.append(matrix[i][i])

if refl.count(1) == side:
    print('Матрица рефлексивна')
elif refl.count(0) == side:
    print('Матрица антирефлексивна')
else:
    print('Матрица не является ни рефлексивной, ни антирефлексивной')

# Проверка симметричности
if matrix == matrix_transp:
    print('Матрица симметрична')
else:
    print('Матрица не симметрична')

# Проверка антисимметричности (https://ru.frwiki.wiki/wiki/Matrice_antisymétrique)
if matrix == matrix_transp_neg:
    print('Матрица антисимметрична')
else:
    print('Матрица не антисимметрична')

# Проверка транзитивности (https://math.stackexchange.com/questions/228898/how-to-check-whether-a-relation-is-transitive-from-the-matrix-representation)

matrix_np = np.array([elem[i:i+side] for i in range(0,len(elem),side)])
matrix_sqr = matrix_np.dot(matrix_np)

zeros_sqr = []

k = 0
for i in range(len(matrix_sqr)):
    for j in matrix_sqr[i]:
        k += 1
        if j == 0:
            zeros_sqr.append(k)

zeros = []

k = 0
for i in range(len(matrix)):
    for j in matrix[i]:
        k += 1
        if j == 0:
            zeros.append(k)

res = []
for el in zeros:
    if el in zeros_sqr:
        res.append(True)
    else:
        res.append(False)

if res.count(True) == len(res):
    print('Матрица транзитивна')
else:
    print('Матрица не транзитивна')

# 1 1 1 1 0 0 1 1 0 1 1 1 0 1 0 0
# 1 1 1 0 0 1 1 0 0 0 1 1 1 0 0 1
# 0 1 1 0 1 1 0 0 0
# 2 1 5 -4 1 6 3 -9 5 3 8 7 -4 -9 7 3
# 0 -4 5 9 4 0 -1 8 -5 1 0 -2 -9 -8 2 0
# 0 1 -2 -1 0 3 2 -3 0
# 1 0 1 0 1 0 1 0 1
# 0 1 0 0 1 0 0 1 0
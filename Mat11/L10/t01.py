from base import *

#  Main program
n = int(input())
a = readMatrix(n)
# printMatrix(a)

counter = 0
suma = 0
for row in a:
    for el in row:
# n = len(a)  # кількість рядків матриці
# m = len(a[0])  # кількість стовчиків матриці
# for i in range(n):
#     for j in range(m):
#         el = a[i][j]
        if el < 0 and el % 2 == 0:
            counter += 1
            suma += el

print(counter, suma)

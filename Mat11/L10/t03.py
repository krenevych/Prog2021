from base import *

n = int(input())
M = []
for i in range(n):
    row = [0] * n  # [0, 0, ..., 0]
    M.append(row)

for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            # i та j таке, що елемент НАД побічною діагоналлю:
            M[i][j] = 2
        elif i + j > n - 1:
            # i та j таке, що елемент ПІД побічною діагоналлю:
            M[i][j] = 1

printMatrix(M, "%d")

def printMatrix(M, elementView="%4d"):
    for row in M:
        for el in row:
            print(elementView % el, end= "")
        print()


n = int(input())

M = []
for i in range(n):
    row = [0] * n
    M.append(row)

for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            # елемент над головною діагоналлю:
            M[i][j] = 2
        elif i + j > n - 1:
            # елемент під головною діагоналлю:
            M[i][j] = 1

printMatrix(M, "%d")
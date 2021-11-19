# from base import printMatrix, readMatrix
def readMatrix(n, typeElements=int):
    M = []
    for i in range(n):
        row = [typeElements(el) for el in input().split()]
        M.append(row)
        # print("row %d" % i, row)
    return M

def printMatrix(M, sep="", format="%4d"):
    for row in M:
        for el in row:
            print(format % el, end=sep)
        print()


def multMatrix(a, b):
    row_c = len(a)
    col_c = len(b[0])
    #  створюємо матрицю заповнену нулями
    c = []
    for i in range(row_c):
        row = [0] * col_c
        c.append(row)
    #     множення
    n = len(b) # n = len(a[0])
    for i in range(row_c):
        for j in range(col_c):
            for r in range(n):
                c[i][j] += a[i][r] * b[r][j]

    return c


# Головна програма

m_A, n_A = [int(el) for el in input().split()]
A = readMatrix(m_A)

n_B, q_B = [int(el) for el in input().split()]
B = readMatrix(n_B)

if n_A != n_B:
    print(-1)
else:
    C = multMatrix(A, B)
    print(len(C), len(C[0]))
    printMatrix(C, format="%d", sep=" ")

# print("--- A ---")
# printMatrix(A)
# print("--- B ---")
# printMatrix(B)





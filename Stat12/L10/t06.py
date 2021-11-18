# from base import readMatrix, printMatrix

def readMatrix(n, elementsType=int):
    M = []
    for i in range(n):
        row = [elementsType(el) for el in input().split()]
        M.append(row)

    return M

def printMatrix(M, elementView="%4d", endElem=""):
    for row in M:
        for el in row:
            print(elementView % el, end=endElem)
        print()

def multMatrix(a, b):
    row_count_c = len(a)
    col_count_c = len(b[0])
    # створення матриці заповненої нулями
    c = []
    for i in range(row_count_c):
        row = [0] * col_count_c
        c.append(row)

    # множення
    n = len(b)  # n = len(a[0])
    for i in range(row_count_c):
        for j in range(col_count_c):
            for r in range(n):
                c[i][j] += a[i][r] * b[r][j]

    return c


m_A, n_A = [int(el) for el in input().split()]
A = readMatrix(m_A)

n_B, q_B =  [int(el) for el in input().split()]
B = readMatrix(n_B)


if n_A == n_B:
    C = multMatrix(A, B)
    print(len(C), len(C[0]))
    printMatrix(C, endElem=" ", elementView="%d")
else:
    print(-1)

# printMatrix(A)
#
# printMatrix(B)




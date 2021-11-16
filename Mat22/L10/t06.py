def writeMatrix(M):
    for row in M:  # row - рядок матриці
        for a in row:  # a - елемент рядка
            print(a, end=" ")
        print()

def readMatrix():
    na, ma = [int(el) for el in input().split()]
    A = []  # Матриця - список списків - колекція рядків матриці
    # По-рядкове зчитування матриці з клавіатури
    for i in range(na):
        row = [int(el) for el in input().split()]
        A.append(row)
    return A

def multMatrix(A, B):
    m = len(A)
    n = len(B)
    q = len(B[0])
    C = []
    for i in range(m):
        row = [0] * q
        C.append(row)

    for i in range(m):
        for j in range(q):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

# writeMatrix(A)
# print("============")
# writeMatrix(B)
# print("============")

A = readMatrix()
B = readMatrix()
if len(A[0]) != len(B):
    print(-1)
else:
    C = multMatrix(A, B)
    print(len(C), len(C[0]))
    writeMatrix(C)
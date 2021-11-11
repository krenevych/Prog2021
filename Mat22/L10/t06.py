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
    n = len(B[0])
    for i in range()


A = readMatrix()
B = readMatrix()

writeMatrix(A)
writeMatrix(B)
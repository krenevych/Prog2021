def readMatrix(n):
    M = []
    for i in range(n):
        row = [int(el) for el in input().split()]
        M.append(row)
        # print("row %d" % i, row)
    return M

def printMatrix(M):
    for row in M:
        for el in row:
            print("%4d" % el, end="")
        print()

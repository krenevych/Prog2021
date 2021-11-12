def readMatrix(n):
    M = []
    for i in range(n):
        row = [int(el) for el in input().split()]
        M.append(row)
        # print("row %d" % i, row)
    return M

def printMatrix(M, format="%4d"):
    for row in M:
        for el in row:
            print(format % el, end="")
        print()

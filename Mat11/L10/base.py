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

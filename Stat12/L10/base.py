def readMatrix(n, elementsType=int):
    M = []
    for i in range(n):
        row = [elementsType(el) for el in input().split()]
        M.append(row)

    return M

def writeMatrix(M, elementsType=int):
    # n = len(M)  # кількість рядків матриці
    # m = len(M[0]) # кількість стовпчиків матриці
    if elementsType == int:
        str_elem = "%4d"
    elif elementsType == float:
        str_elem = "%7.2f"
    else:
        str_elem = "%5s"

    for row in M:
        # print(*row)
        for el in row:
            print(str_elem % el, end= "")
        print()


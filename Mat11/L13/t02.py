def sumInFile(fname):
    suma = 0
    f = open(fname)

    for line in f:
        # print(line, end="")
        lstNum = [int(el) for el in line.split()]
        # print(lstNum)
        suma += sum(lstNum)

    f.close()
    return suma


res = sumInFile("prime.txt")
print(res)
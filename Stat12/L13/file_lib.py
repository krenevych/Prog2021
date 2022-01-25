def calculateSum(fname):
    suma = 0
    f = open(fname)
    for line in f:
        a = [float(el) for el in line.split()]
        suma += sum(a)
    f.close()
    return suma


if __name__ == "__main__":
    print(calculateSum("input13_2.txt"))

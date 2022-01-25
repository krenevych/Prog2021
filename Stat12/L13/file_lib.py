def calculateSum(fname):
    suma = 0
    f = open(fname)
    for line in f:
        a = [float(el) for el in line.split()]
        suma += sum(a)
    f.close()
    return suma

def countNeg(fname):
    counter = 0
    f = open(fname)
    for line in f:
        a = [float(el) for el in line.split()]
        for el in a:
            if el < 0:
                counter += 1
    f.close()
    return counter


if __name__ == "__main__":
    # print(calculateSum("input13_2.txt"))
    print(countNeg("input13_2.txt"))

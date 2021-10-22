def max2(a, b):
    return a if a > b else b

def min2(a, b):
    return a if a < b else b

def min3(a, b, c):
    p = min2(a, b)
    res = min2(p, c)
    return res


x, y, z = [float(el) for el in input().split()]
res = min3(max2(x, y), max2(y, z), x + y + z)
print("%0.2f" % res)

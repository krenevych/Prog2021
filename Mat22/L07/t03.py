def max2(x, y):
    return x if x > y else y

def min2(x, y):
    return x if x < y else y

def min3(x, y, z):
    return min2(min2(x, y), z)

x, y, z = [float(el) for el in input().split()]
res = min3(max2(x, y), max2(y, z), x + y + z)
print("%0.2f" % res)

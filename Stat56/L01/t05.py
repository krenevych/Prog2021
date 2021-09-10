x1, y1, x2, y2, x3, y3 = [float(d) for d in input().split()]

a = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
b = ((x3 - x2)**2 + (y3 - y2)**2) ** 0.5
c = ((x1 - x3)**2 + (y1 - y3)**2) ** 0.5

p = a + b + c
p2 = p / 2
s = (p2 * (p2 - a) * (p2 - b) * (p2 - c)) ** 0.5

print("%0.4f %0.4f" % (p, s))
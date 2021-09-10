a, b, c = [float(d) for d in input().split()]

m = max(a, b, c)

if a == m:
    a, c = c, a
elif b == m:
    b, c = c, b

if a ** 2 + b ** 2 == c ** 2:
    print("YES")
else:
    print("NO")

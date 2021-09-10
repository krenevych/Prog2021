a, b, c = map(float, input().split())

if (a * a + b * b == c * c
        or a * a + c * c == b * b
        or a * a == b * b + c * c):
    print("YES")
else:
    print("NO")

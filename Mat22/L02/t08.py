a, b, c = map(int, input().split())  # 2 3 4

if a <= b <= c or a >= b >= c:
    print(b)
elif b <= c <= a or b >= c >= a:
    print(c)
else:
    print(a)

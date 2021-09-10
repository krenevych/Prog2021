a, b, c = [int(d) for d in input().split()]

if (a**2 + b**2 == c**2           # 3 4 5
        or a**2 == b**2 + c**2    # 5 4 3
        or b**2 == a**2 + c**2):  # 3 5 4
    print("YES")
else:
    print("NO")

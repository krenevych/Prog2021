a, b, c = [int(el) for el in input().split()]
# a, b, c = map(int, input().split()) # 3 4 5


if (a ** 2 + b ** 2 == c ** 2
           or a ** 2 == b ** 2 + c ** 2
           or b ** 2 == c ** 2 + a ** 2):
    print("YES")
else:
    print("NO")


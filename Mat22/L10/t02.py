n, m = [int(el) for el in input().split()]

for k in range(1, n * m + 1):
    # print("%3d" % k, end=" ")
    print(k, end=" ")
    if k % m == 0:
        print()

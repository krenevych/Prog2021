n = int(input())

res = 0

# 10 .. 99
for i in range(10, 100):
    od = i % 10
    de = i // 10
    if n == 1:
        if de > od: res += 1
    elif n == 2:
        if de < od: res += 1
    elif n == 3:
        if de % 2 == od % 2: res += 1
    elif n == 4:
        if de == od: res += i
    elif n == 5:
        if de % 2 == od % 2 == 0: res += i
    elif n == 6:
        if de % 2 == od % 2 == 1: res += i

print(res)



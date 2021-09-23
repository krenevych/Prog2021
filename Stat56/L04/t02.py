n = int(input())

# 10 .. 99

res = 0

for i in range(10, 100):
    od = i % 10
    dec = i // 10
    if n == 1:
        if dec > od: res += 1
    elif n == 2:
        if dec < od: res += 1
    elif n == 3:
        if dec % 2 == od % 2: res += 1
    elif n == 4:
        if dec == od: res += i
    elif n == 5:
        if dec % 2 == od % 2 == 0 : res += i
    elif n == 6:
        if dec % 2 == od % 2 == 1 : res += i


print(res)
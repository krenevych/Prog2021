n = int(input())

# Обчислити кiлькiсть двозначних чисел, цифри яких спадають.

result = 0
# 10,... 99
for i in range(10, 100):
    # print(i)
    de = i // 10  # десятки
    od = i % 10  # одиниці

    if n == 1:
        if de > od: result += 1
    elif n == 2:
        if de < od: result += 1
    elif n == 3:  # 22: 2 2
        if de % 2 == od % 2: result += 1
    elif n == 4:  # 22: 2 2
        if de == od: result += i
    elif n == 5:  # 22: 2 2
        if de % 2 == od % 2 == 0: result += i
    elif n == 6:  # 22: 2 2
        if de % 2 == od % 2 == 1: result += i


print(result)

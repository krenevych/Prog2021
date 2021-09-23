n = int(input())

# n = 21 -> 3
# n = 19 -> 19

# 21: 3 7
# n = 19:
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        print(i)
        break
else:
    print(n)

pass
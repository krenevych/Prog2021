# Написати програму для обчислення добутку двох
# натуральних чисел, використовуючи лише операцію
# додавання.

# 6 * 4 = 0 + 4 + 4 + 4 + 4 + 4 + 4
# 0 * 4 = 0
n, m = map(int, input().split())  # m * n
i = 0
mult = 0
while i < m:
    mult += n
    i = i + 1

print(mult)
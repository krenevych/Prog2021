# 5! = 1 * 1 * 2 * 3 * 4 * 5
# 0! = 1
# 1! = 0! * 1
# 2! = 1! * 2
n = int(input())
f = 1
i = 1
while i <= n:
    f *= i
    i += 1

print(f)
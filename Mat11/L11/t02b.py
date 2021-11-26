n = int(input())

S = 0

sign = -1
for k in range(1, n + 1):
    sign = -sign
    S = S + sign * 1 / k

print(S)

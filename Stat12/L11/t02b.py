n = int(input("n = "))

S = 0
sign = -1
for i in range(1, n+1):
    sign = -sign
    S += sign * 1 / i

print(S)

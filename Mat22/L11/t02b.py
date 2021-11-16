N = int(input("n = "))

S = 1
sign = 1
for n in range(2, N + 1):
    sign = -sign
    S += sign / n

print(S)
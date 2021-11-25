N = int(input())

P = 2
for n in range(2, N+1):
    P = P * (1 + 1 / (n * n))

print(P)
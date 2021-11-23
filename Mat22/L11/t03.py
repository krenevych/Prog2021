N = int(input("N=?"))

P = 2
for n in range(2, N+1):
    P *= (1 + 1/(n*n))

print(P)
N = 20000

a = 15
S = 1
n = 1
# for n in range(2, N+1):
while S <= a:
    n += 1
    S += 1/n
    # print(S)

print(n, S)
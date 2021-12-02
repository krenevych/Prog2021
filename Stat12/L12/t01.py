
# N = 1000
a = float(input("a = ?"))
S = 1
n = 1
# print(S)
# for n in range(2, N+1):
while S <= a:
    n += 1
    S += 1/n
    # print(n, S)
print(n, S)


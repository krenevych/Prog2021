n = int(input())

# M = []
# for i in range(n):
#     row = [0] * n
#     M.append(row)
#
# for i in range(n):
#     for j in range(n):
#         if i < (n - 1) - j:
#             M[i][j] = 2
#         elif i > (n - 1) - j:
#             M[i][j] = 1

M = []
for i in range(n):
    row = []
    for j in range(n):
        if i < (n - 1) - j:
            row.append(2)
        elif i > (n - 1) - j:
            row.append(1)
        else:
            row.append(0)
    M.append(row)

for row in M:
    print(*row, sep="")
    # print(*row)

# print(M)
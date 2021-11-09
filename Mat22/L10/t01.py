n = int(input())
M = []
for i in range(n):
    row = [int(el) for el in input().split()]
    M.append(row)

counter = 0
suma = 0

# n = len(M)
# m = len(M[0])
# for i in range(n):
#     for j in range(m):
#         if M[i][j] < 0 and M[i][j] % 2 == 0:
#             counter += 1
#             suma += M[i][j]

for row in M: # row - рядок матриці
    for a in row:  # a - елемент рядка
        if a < 0 and a % 2 ==0:
            counter += 1
            suma += a

print(counter, suma)


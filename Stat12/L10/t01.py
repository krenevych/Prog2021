import base

n = int(input())
A = base.readMatrix(n)

counter = 0
suma = 0
for row in A:
    # print(*row)
    for el in row:
        if el < 0 and el % 2 == 0:
            counter += 1
            suma += el

print(counter, suma)
# base.writeMatrix(A)

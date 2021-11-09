n = int(input())
M = [] # Матриця - список списків - колекція рядків матриці

# По-рядкове зчитування матриці з клавіатури
for i in range(n):
    row = [int(el) for el in input().split()]
    M.append(row)

# print(M)

# поелементний прохід матриці (індексний)
n = len(M)
m = len(M[0])
for i in range(n):
    for j in range(m):
        print(M[i][j])

# поелементний прохід матриці - варіант 2
for row in M: # row - рядок матриці
    for a in row:  # a - елемент рядка
        print(a)
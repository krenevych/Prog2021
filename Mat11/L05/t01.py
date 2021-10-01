N = int(input())
array = [int(a) for a in input().split()]

# M = max(array)

M = array[0]
# for i in range(1, len(array)):
for i in range(1, N):
    if M < array[i]:
        M = array[i]

print(M)

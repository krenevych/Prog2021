N = int(input())
array = [int(a) for a in input().split()]

# for a in array:
#     if a >= 0:
#         a += 2

for i in range(N):
    if array[i] >= 0:
        array[i] += 2

# for a in array:
#     print(a, end=" ")
print(*array)  # print(array[0], array[1], array[2], ... )

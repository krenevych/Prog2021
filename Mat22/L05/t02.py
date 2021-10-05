N = int(input())
lst = [int(el) for el in input().split()]

# for el in lst:
#   if el > 0:
#     el += 2

for i in range(N):
    if lst[i] >= 0:
        lst[i] += 2

print(*lst)  #print(lst[0], lst[1], lst[2], ...)
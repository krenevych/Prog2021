N = int(input())
lst = [int(el) for el in input().split()]
# print(max(lst))

maxy = lst[0]
# for i in range(len(lst)):
for i in range(1, N):
    # print(i)
    el = lst[i]
    if el > maxy:
        maxy = el

print(maxy)
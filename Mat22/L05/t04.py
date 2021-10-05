n = int(input())

lst = []
for i in range(n):
    el = int(input())
    # print(el)
    lst.append(el)

for i in range(n // 2):
    lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]

print(*lst)
# print(lst[start : end : step])
# print(*lst[ :  : -1]) # реверс з використанням зрізу


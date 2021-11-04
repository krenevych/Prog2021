N = int(input())
lst = [int(el) for el in input().split()]

# print(lst)

freq = {}
for a in lst:
    if a in freq:
        freq[a] += 1
    else:
        freq[a] = 1

# print(freq)
# 0 1 -2 1 0 0 3

k = []
for el in lst[::-1]:
    if freq[el] > 1 and el not in k:
        k.insert(0, el)

if len(k) == 0:
    print("NO")
else:
    print(*k)









# and el not in k
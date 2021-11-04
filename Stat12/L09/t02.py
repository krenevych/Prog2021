n = int(input())
a = [int(el) for el in input().split()]
# print(a)

freq = {el: a.count(el) for el in a}

# print(freq)

major = None
n_2 = n // 2
for key, val in freq.items():
    if val > n_2:
        major = key

if major:
    print(major)
else:
    print(-1)

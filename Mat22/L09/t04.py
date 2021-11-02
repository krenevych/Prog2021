n = int(input())
a = [int(el) for el in input().split()]
freq = {el: a.count(el) for el in a}

non_uniq = set()
for key, val in freq.items():
    if val > 1:
        non_uniq.add(key)

if len(non_uniq) == 0:
    print("NO")
else:
    res = []
    for k in a[::-1]:
        if k in non_uniq:
            res.append(k)
            non_uniq.remove(k)

    print(*(res[::-1]))
# print(freq)
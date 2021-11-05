n = int(input())
array = [int(el) for el in input().split()]

freq = {el: array.count(el) for el in set(array)}

non_uniq = []
for a in array[::-1]:
    if freq[a] > 1 and a not in non_uniq:
        non_uniq.append(a)
        # print(a, end=" ")

if len(non_uniq) == 0:
    print("NO")
else:
    print(*non_uniq[::-1])

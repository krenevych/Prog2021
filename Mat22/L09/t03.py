n = int(input())
a = [int(el) for el in input().split()]

ms = {}
for el in a:
    if el in ms:
        ms[el] += 1
    else:
        ms[el] = 1


for el in a:
    if ms[el] == 1:
        print(el, end=" ")

# for i in ms:
#     if ms.get(i) == 1:
#         print(i, end=" ")


N = int(input())
lst = [int(el) for el in input().split()]

freq = {}
for a in lst:
    if a in freq:
        freq[a] += 1
    else:
        freq[a] = 1

# for key, val in freq.items():
#     if val == 1:
#         print(key, end=" ")

for el in lst:
    if freq[el] == 1:
        print(el, end=" ")


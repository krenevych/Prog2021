N = int(input())
array = [int(el) for el in input().split()]

freq = {el: array.count(el) for el in set(array)}
# print(freq)

for a in array:
    if freq[a] == 1:
        print(a, end=" ")

# for key, val in freq.items():
#     if val == 1:
#         print(key, end=" ")


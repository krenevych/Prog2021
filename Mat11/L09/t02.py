n = int(input())
array = [int(el) for el in input().split()]

freq = {}
for a in array:
    if a in freq:
        freq[a] += 1
    else:
        freq[a] = 1

# for key in freq:
#     if freq[key] > n // 2:
for key, val in freq.items():
    if val > n // 2:
        print(key)
        break
else:
    print(-1)
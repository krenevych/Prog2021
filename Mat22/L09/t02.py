N = int(input())
a = [int(el) for el in input().split()]
# print(a)

# freq = {el: a.count(el) for el in a}

freq = {}
for el in a:
    if el in freq:
        freq[el] += 1
    else:
        freq[el] = 1

# print(freq)

n_2 = N // 2

max_key = 0
max_val = 0
for key, val in freq.items():
    if val > max_val:
        max_key = key
        max_val = val

# print(max_key, max_val)

if max_val > n_2:
    print(max_key)
else:
    print(-1)

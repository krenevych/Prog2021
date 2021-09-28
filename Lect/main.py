
lst = [int(el) for el in input().split()]

suma = 0

# for el in lst:
#     suma += el

maximum = lst[0]
max_index = 0
for i in range(1, len(lst)):
    if maximum < lst[i]:
        maximum = lst[i]
        max_index = i


print(maximum)
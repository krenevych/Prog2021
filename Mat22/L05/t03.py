N = int(input())
lst = [float(el) for el in input().split()]

count = 0
suma = 0
for i in range(2, N, 3):
    # print(f"{i+1} : {lst[i]}")
    if lst[i] > 0:
        count += 1
        suma += lst[i]

# print(f"{count} {suma: 0.2f}")
print("%d %0.2f" % (count, suma))

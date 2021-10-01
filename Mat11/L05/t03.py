N = int(input())
array = [float(a) for a in input().split()]

suma = 0
counter = 0
for i in range(2, N, 3):
    if array[i] > 0:
        counter += 1
        suma += array[i]

print("%d %0.2f" % (counter, suma))
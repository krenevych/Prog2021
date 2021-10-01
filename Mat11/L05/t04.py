N = int(input())

array = []
for i in range(N):
    a = int(input())
    array.append(a)

# скористаємося зрізом з від'ємним кроком -1
# print(*array[::-1])

# Пробігаємо масив з кінця і виводимо кожен елемент
# for i in range(N-1, -1, -1):
#     print(array[i], end=" ")

for i in range(N // 2):
    array[i], array[len(array) - 1 - i] = array[len(array) - 1 - i], array[i]
print(*array)
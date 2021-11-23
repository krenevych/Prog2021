n = int(input("n = ?"))
S = 0
i = 0
while i < n:
    try:
        a = int(input())
        S += a
        i += 1
    except ValueError:
        print("Введене число не є цілим")

print(S)
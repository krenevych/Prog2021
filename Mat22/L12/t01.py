# N = int(input("N: "))
a = float(input("a = ? "))

S = 1
n = 1
# for n in range(2, N + 1):
while S <= a:
    n += 1
    S = S + 1 / n
    print(f"{n}: {S}")

print("====== S > a ========")
print(S)



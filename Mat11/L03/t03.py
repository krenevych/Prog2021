# Знайти значення факторіалу цілого числа n.
# n = 5: 5! = 1 * 1 * 2 * 3 * 4 * 5

n = int(input())

fact = 1
i = 0

while i < n:
    i += 1
    fact *= i

print(fact)


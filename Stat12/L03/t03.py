# Знайти значення факторіалу цілого числа n.
# 3! = 1 * 1 * 2 * 3
# 0! = 1
n= int(input())
fact = 1
i = 0
while i < n:
    i += 1
    fact *= i

print(fact)

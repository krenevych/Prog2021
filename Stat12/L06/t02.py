expr = input()

counter = 0

for c in expr.upper():
    if c in "AEIOUY":
        counter += 1

print(counter)
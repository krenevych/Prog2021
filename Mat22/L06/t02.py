s = input()

counter = 0
for ch in s:
    # A, E, I, O, U і Y
    if ch in "AEIOUY":
        counter += 1

print(counter)
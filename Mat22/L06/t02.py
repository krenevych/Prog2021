s = input()

counter = 0
for ch in s:
    if ch in "AEIOUY":
        counter += 1

print(counter)


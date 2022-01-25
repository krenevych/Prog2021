
f = open("input.txt", encoding="utf-8")

max1 = f.readline()
for line in f:
    if len(max1) < len(line):
        max1 = line

f.close()

print(max1)


f = open("input.txt", encoding="UTF-8")


print("Пункт a:")
i = 1
for line in f:
    print("line", i, line, end="")
    i += 1
f.close()

print("Пункт b:")

f = open("input.txt", encoding="UTF-8")
for line in f:
    # print(len(line))
    if len(line) > 60:
        print(line, end="")
f.close()


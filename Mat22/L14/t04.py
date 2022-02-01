
fname = input("Задайтей ім'я файлу ")

try:
    f = open(fname, encoding="utf-8")
    for line in f:
        print(line, end="")
    f.close()
except FileNotFoundError as e:
    print(e)



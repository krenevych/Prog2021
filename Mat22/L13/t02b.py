# У текстовому файлі записана непорожня
# послідовність дійсних чисел, які розділяються
# пропусками. Визначити функції для обчислення:
# a)	суми компонент файла;

f = open("input2.txt")
counter_neg = 0
for line in f:
    # a = [float(el) for el in line.split()]
    print(line.split())
    a = map(float, line.split())
    for el in a:
        # print(el)
        if el < 0:
            counter_neg += 1

print(counter_neg)
f.close()

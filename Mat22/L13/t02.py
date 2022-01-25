# У текстовому файлі записана непорожня
# послідовність дійсних чисел, які розділяються
# пропусками. Визначити функції для обчислення:
# a)	суми компонент файла;

f = open("input2.txt")
suma = 0
for line in f:
    # a = [float(el) for el in line.split()]
    a = map(float, line.split())
    # print(a)
    suma += sum(a)

print(suma)
f.close()

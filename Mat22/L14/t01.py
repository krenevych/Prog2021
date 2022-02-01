# Знайти площу трикутника за трьома сторонами a,b,c.
# Оформити перевірку вхідних даних (що трикутник з такими сторонами a,b,c існує)
# за допомогою оператора assert.

while True:
    a, b, c = [float(el) for el in input("Введіть сторони трикутника: ").split()]
    # print(a, b, c)
    try:
        assert a + b > c and b + c > a and a + c > b
        p = (a + b + c) / 2
        s = p * (p - a) * (p - b) * (p - c)
        s = s ** 0.5
        print("Площа нашого трикутника = ", s)
        break
    except AssertionError:
        print("Трикутника зі вказаними сторонами не існує!")







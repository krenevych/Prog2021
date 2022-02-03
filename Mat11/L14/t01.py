# Знайти площу трикутника за трьома сторонами a,b,c.
# Оформити перевірку вхідних даних (що трикутник з такими сторонами a,b,c існує)
# за допомогою оператора assert.

while True:
    try:
        a, b, c = map(float, input("Введіть сторони трикутника: ").split())
        assert a + b > c and a + c > b and b + c > a, "Трикутника з такими сторонами не існує!"
        p = (a + b + c) / 2.0
        s = p * (p - a) * (p - b) * (p - c)
        s = s ** 0.5
        print("Площа трикутника = ", s)
    except ValueError:
        print("Введіть дані правильно!")
    except AssertionError as e:
        print(e)
    else:
        break

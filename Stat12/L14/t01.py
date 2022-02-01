while True:
    try:
        a, b, c = map(float, input("Введіть сторони трикутника: ").split())
        assert a + b > c and a + c > b and b + c > a
        p = (a + b + c) / 2
        s = p * (p - a) * (p - b) * (p - c)
        print("Площа заданого трикутника = ", s ** 0.5)
    except ValueError:
        print("Введіть дані правильно!!!")
    except AssertionError:
        print("Трикутника зі вказаними сторонами не існує! Спробуйте ще раз!")
    else:
        break

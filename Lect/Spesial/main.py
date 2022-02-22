class Polinom:
    def __init__(self, coefs: dict):
        self.coefs = coefs

    def print(self):
        pows = list(self.coefs.keys())
        pows.sort()
        for pow in pows[::-1]:
            print(f"{self.coefs[pow]}x^{pow} + ", end="")
        print()

    def __call__(self, x):
        res = 0
        for pow, coef in self.coefs.items():
            res += coef * x**pow
        return res


# 4x^2 + 3x + 2
y = Polinom({2:4, 1:3, 0:2})
y.print()
f = y(1)
print(f)
print(y.__call__(1))

from Figure import *

class Auto(Figure) :

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

        self.components = []
        body = Rectangle(x + 0, y + 0, 200, 50, color)
        top = Triangle(x + 50, y + 50, 100, color)
        wheel1 = Circle(x + 25, y - 25, 25, "black")
        wheel2 = Circle(x + 150, y -25, 25, "black")
        self.components.append(body)
        self.components.append(top)
        self.components.append(wheel1)
        self.components.append(wheel2)

    def _draw(self, color):
        for component in self.components:
            component._draw(color)

    def move(self, dx, dy):
        for component in self.components:
            component.move(dx, dy)


if __name__ == '__main__':
    speed(0)
    auto = Auto(0, 0, "red")
    auto.show()
    # auto.hide()
    auto.move(-300, 100)

    mainloop()



from turtle import *

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):

        # додати перевірку, що всі три точки не лежать на одній прямій

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._x3 = x3
        self._y3 = y3
        self._color = "black"
        self._penSize = 1

    def setColor(self, color):
        self._color = color

    def setPenSize(self, size):
        self._penSize = size

    def draw(self):
        up()
        pencolor(self._color)
        pensize(self._penSize)
        goto(self._x1, self._y1)
        down()
        goto(self._x2, self._y2)
        goto(self._x3, self._y3)
        goto(self._x1, self._y1)
        up()


if __name__ == '__main__':
    t = Triangle(-100, -100, 100, -100, 0, 100)
    t.setColor("blue")
    t.setPenSize(10)
    t.draw()


    mainloop() # щоб не закривалось вікно
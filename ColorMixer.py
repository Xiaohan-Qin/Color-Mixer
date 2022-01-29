from turtle import Turtle
from color_mixer import set_bg_color


class ColorMixer(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape("turtle")
        self.resizemode("user")
        self.shapesize(3, 3, 5)
        self.pensize(7)
        self._color = [0, 0, 0]
        self.x = x
        self._color[x] = y
        r, g, b = self._color[0], self._color[1], self._color[2]
        self.color(r, g, b)
        self.speed(0)
        self.left(90)
        self.pu()
        self.goto(x, 0)
        self.pd()
        self.sety(1)
        self.pencolor("gray25")
        self.ondrag(self.shift)

    def shift(self, x, y):
        self.sety(max(0, min(y, 1)))
        self._color[self.x] = self.ycor()
        r, g, b = self._color[0], self._color[1], self._color[2]
        self.fillcolor(r, g, b)
        set_bg_color()





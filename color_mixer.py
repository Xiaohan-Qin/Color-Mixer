import turtle
from turtle import Turtle, Screen


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

        # drag turtle to change y-axis coordinates
        self.ondrag(self.shift)

    def shift(self, x, y):
        self.sety(max(0, min(y, 1)))

        # assign colormode values by y-axis coordinates
        self._color[self.x] = self.ycor()
        r, g, b = self._color[0], self._color[1], self._color[2]

        # mix and fill background color by colormode values
        self.fillcolor(r, g, b)
        set_bg_color()


def set_bg_color():
    screen.bgcolor(red.ycor(), green.ycor(), blue.ycor())


def main():
    global screen, red, green, blue
    screen = Screen()

    # set up colormode scope as 1
    screen.colormode(1.0)

    # set up my own coordinate system
    screen.setworldcoordinates(-1, -0.5, 3, 1.6)

    # Initialize primary colors' locations
    red = ColorMixer(0, 0.5)
    green = ColorMixer(1, 0.5)
    blue = ColorMixer(2, 0.5)
    set_bg_color()

    writer = Turtle()
    writer.ht()
    writer.pu()
    writer.goto(1, 1.2)
    writer.write("Drag to mix!", align="center", font=("Arial", 30, "normal"))
    return "EVENTLOOP"


if __name__ == "__main__":
    msg = main()
    print(msg)
    turtle.mainloop()

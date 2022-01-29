from ColorMixer import ColorMixer
import turtle
from turtle import Turtle, Screen


def set_bg_color():
    screen.bgcolor(red.ycor(), green.ycor(), blue.ycor())


def main():
    global screen, red, green, blue
    screen = Screen()
    screen.colormode(1.0)
    screen.setworldcoordinates(-1, -0.5, 3, 1.6)

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

    
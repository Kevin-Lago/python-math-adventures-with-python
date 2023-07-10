from turtle import *
from time import sleep


def square(size: int = 100):
    for _ in range(4):
        forward(size)
        right(90)


def triangle(size: int = 100):
    for _ in range(3):
        forward(size)
        right(120)


def polygon(size: int = 100, sides: int = 4):
    for i in range(sides):
        forward(size)
        right(360 / sides)


def turtle_spiral():
    size = 5

    for _ in range(60):
        square(size)
        size += 5
        right(5)


def star(size: int = 100):
    for _ in range(5):
        forward(size)
        right(144)


def star_spiral():
    size = 5

    for _ in range(60):
        star(size)
        size += 5
        right(10)


if __name__ == '__main__':
    shape('turtle')
    speed(0)

    star_spiral()
    sleep(2)
    clear()

    star(100)
    sleep(2)
    clear()

    turtle_spiral()
    sleep(2)
    clear()

    polygon(100, 6)
    sleep(2)
    clear()

    triangle()
    sleep(2)
    clear()

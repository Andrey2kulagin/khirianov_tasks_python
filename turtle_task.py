import turtle
import math
import time

def squaring():
    len_str = 10

    for i in range(1, 11):
        turtle.penup()
        turtle.setpos(-(len_str * i) / 2, -(len_str * i) / 2)
        turtle.down()
        for j in range(4):
            turtle.forward(i * len_str)
            turtle.left(90)


def spiral():
    n = 1
    for j in range(100000):
        if j % 10 == 0:
            n += 1
        turtle.forward(n)
        turtle.left(5)


def pauk(n):
    for i in range(1, n + 1):
        turtle.setpos(0, 0)
        turtle.down()
        turtle.seth(360 / n * i)
        turtle.forward(100)
        turtle.stamp()
        turtle.penup()


def squar_pauk():
    for j in range(100000):
        turtle.forward(5 * j)
        turtle.left(90)


def true_mnog(n):
    a = (n - 2) * 180 / n
    cure_len = 5 * n
    r = cure_len / (math.sin(360 * 0.0174533 / 2 / n) * 2)
    print(cure_len, r)
    turtle.penup()
    turtle.setpos(turtle.xcor() + r * 3, 0)
    turtle.seth(0)
    # turtle.forward(r)
    # turtle.seth(180);
    turtle.down()
    for i in range(n):
        if i == 0:
            turtle.left(180 - a / 2)
            turtle.forward(r)
        else:
            turtle.left(180 - a)
            turtle.forward(r)

        turtle.forward(cure_len * n)


def circle():
    for i in range(100):
        turtle.forward(1)
        turtle.left(360 / 100)


def circle_with_r(r):
    for i in range(100):
        turtle.forward(r)
        turtle.left(360 / 100)


def flower(n):
    for i in range(1, 9):
        turtle.left(360 / i)
        circle()


def butterfly():
    n = 8
    j = 0
    for i in range(n):
        if i % 2 == 0:
            turtle.seth(90)
            j += 1
        else:
            turtle.seth(270)
        circle_with_r(j * 2)

def arc(r):
    for i in range(50):
        turtle.forward(r)
        turtle.right(360 / 100)
def spring(n):
    turtle.seth(90)
    for i in range(n):
        arc(2)
        arc(0.4)

def eay(n):
    turtle.color("black", "blue")
    turtle.begin_fill()
    turtle.penup()
    turtle.setpos(n*80, 200)
    turtle.down()
    circle_with_r(1)
    turtle.end_fill()

def nose():
    turtle.penup()
    turtle.setpos(0, 150)
    turtle.seth(270)
    turtle.width(20)
    turtle.down()
    turtle.forward(20)

def mouth():
    turtle.penup()
    turtle.width(20)
    turtle.color("red")
    turtle.setpos(130, 130)
    turtle.down()
    arc(7)
def smile():
    turtle.color("black", "yellow")
    turtle.begin_fill()
    circle_with_r(10)
    turtle.end_fill()
    eay(-1)
    eay(1)
    nose()
    mouth()

def star(n):
    alf = 180/n
    for i in range(n):
        turtle.left(180-alf)
        turtle.forward(50)
turtle.shape('turtle')
#star(5)
star(10)
#star(8)

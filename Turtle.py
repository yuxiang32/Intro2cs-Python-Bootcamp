import math
import random
import turtle
import time


def rectangle():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)


rectangle()

turtle.circle(20)
turtle.circle(30)

turtle.forward(100)

turtle.circle(20)
turtle.circle(30)

turtle.penup()
turtle.goto(20, -30)
turtle.pendown()

turtle.circle(10)

turtle.penup()
turtle.goto(80, -30)
turtle.pendown()

turtle.circle(10)

turtle.penup()
turtle.goto(45, -50)
turtle.pendown()


def triangle():
    turtle.forward(15)
    turtle.left(120)
    turtle.forward(15)
    turtle.left(120)
    turtle.forward(15)
    turtle.left(120)

triangle()

turtle.penup()
turtle.goto(35, -70)
turtle.pendown()

turtle.right(90)
turtle.circle(20, 180)

turtle.penup()
turtle.goto(-50, 100)

turtle.done()

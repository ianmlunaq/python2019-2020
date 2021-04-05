import turtle
import math
import random
# global variable(s)
# define global variables here
x = 200


def mike(t):
    # change global variables
    # example :  global xM = 200
    t.home()
    t.penup()
    t.backward(globalvar)
    t.pendown()
    t.forward(800)


def circles(t):
    #global x
    for y in range(x):
        t.circle(y)


def triangles(t):
    for y in range(x):
        t.circle(y, 360, 3)


def main():
    try:
        turtle.TurtleScreen._RUNNING = True
        turtle.screensize(canvwidth=700, canvheight=700, bg=None)
        # print(turtle.Screen().screensize())
        w = turtle.Screen()
        t = turtle.Turtle()
        w.bgcolor('black')
        t.color('cornflowerblue')
        t.speed(0)
        t.hideturtle()
        t.home()
        circles(t)
        t.home()
        t.seth(180)
        t.color('coral')
        triangles(t)
        t.pu()
        t.home()
        t.seth(0)
        t.color('white')
        t.forward(100)
        t.seth(270)
        t.pd()
        t.pensize(5)
        t.forward(50)
        t.pu()
        t.home()
        t.seth(0)
        t.forward(200)
        t.seth(270)
        t.pd()
        t.forward(100)
        t.pu()
        t.home()
        t.seth(180)
        t.forward(100)
        t.seth(270)
        t.pd()
        t.pensize(5)
        t.forward(50)
        t.pu()
        t.home()
        t.seth(180)
        t.forward(200)
        t.seth(270)
        t.pd()
        t.pensize(5)
        t.forward(100)

        t.pu()
        t.home()
        t.seth(180)
        t.forward(300)
        t.seth(270)
        t.pd()
        t.pensize(5)
        t.forward(150)

        t.pu()
        t.home()
        t.seth(0)
        t.forward(300)
        t.seth(270)
        t.pd()
        t.pensize(5)
        t.forward(150)

        w.exitonclick()
    finally:
        turtle.Terminator()


print('hello')

if __name__ == '__main__':
    main()

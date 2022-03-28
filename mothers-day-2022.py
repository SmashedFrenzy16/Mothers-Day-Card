from turtle import *
import turtle
from random import randint
import random


pen = turtle.Turtle()
pen.speed("fastest")
s = turtle.Screen()
s.setup(width=1000, height=700)

colormode(255)

global colors

colors = ["red", "blue", "yellow", "green", "lightgreen", "purple", "pink"]

global rand_colors

rand_colors = random.choice(colors)

def curve():

    for i in range(200):

        pen.right(1)
        pen.forward(1)

def heart():

    pen.pendown()
    
    pen.begin_fill()

    pen.left(140)
    pen.forward(113)

    curve()

    pen.left(120)

    curve()

    pen.forward(112)

    pen.end_fill()

def text():

    pen.penup()

    pen.home()

    pen.color('black')

    pen.pendown()


    style = ('Courier', 20, 'normal')
    pen.write('Happy Mother\'s Day!', font=style, align='center')
    pen.hideturtle()

def flower():
    pen.pendown()


    pen.begin_fill()

    for i in range(5):
        pen.circle(30, 180)
        pen.right(108)
    
    pen.end_fill()

    pen.penup()

def star():

    size = 40

    angle = 120

    pen.begin_fill()

    for side in range(5):
        pen.forward(size)
        pen.right(angle)
        pen.forward(size)
        pen.right(72 - angle)
    
    pen.end_fill()


for i in range(10):

    pen.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))

    pen.penup()

    pen.goto(randint(-500, 500), randint(-300, 270))

    pen.pendown()

    

    flower()

    pen.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))

    pen.penup()

    pen.goto(randint(-500, 500), randint(-300, 270))

    pen.pendown()
    

    heart()

    pen.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))

    pen.penup()

    pen.goto(randint(-500, 500), randint(-300, 270))

    pen.pendown()

    star()


text()

while True:
    s.update()


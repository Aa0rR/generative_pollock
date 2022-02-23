import turtle
import random
import os 
import sys
from tkinter import *
from tkinter import colorchooser
#8ed6cc
#f1baa4

color_code = {}
def choose_color(name):
    color_code['rgb'], color_code['hex'] = colorchooser.askcolor(title ="Choose the "+name+" color",color="")
    return color_code['hex']
 
#def setPosition(line):
#   line.setpos(random.randint(0,1000),random.randint(0,1000))

bg=turtle.Screen()
bg.bgcolor(choose_color("background"))

colors = [choose_color("first"), choose_color("second"),choose_color("third"), choose_color("fourth")]

a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
a.hideturtle()
b.hideturtle()
c.hideturtle()

a.up()
b.up()
c.up()
while(True):
 a.setpos(random.randint(0,1000),random.randint(0,1000))
 b.setpos(random.randint(0,1000),random.randint(0,1000))
 c.setpos(random.randint(0,1000),random.randint(0,1000))
 #setPosition(b)
 #setPosition(c)
 
 a.down()
 b.down()
 c.down()

 a.pensize(random.randint(5, 10))
 a.speed(random.randint(4000, 5000))
 a.color(random.choice(colors))

 b.pensize(random.randint(5, 10))
 b.speed(random.randint(4000, 5000))
 b.color(random.choice(colors))

 c.pensize(random.randint(5, 10))
 #a.goto(random.randint(x/2, x),random.randint(y/2, y))
 c.speed(random.randint(4000, 5000))
 c.color(random.choice(colors))

 if(random.randint(1, 50) % 2) == 0:
    a.rt(random.randint(45, 270))
    b.rt(random.randint(45, 270))
    c.rt(random.randint(45, 270))
 else:
    a.lt(random.randint(45, 270))
    a.circle(random.randint(20, 5000))
    b.lt(random.randint(45, 270))
    b.circle(random.randint(20, 5000))
    c.lt(random.randint(45, 270))
    c.circle(random.randint(20, 5000))

 fa = random.randint(25, 1000)
 fb = random.randint(25, 100)
 fc = random.randint(25, 100)

 a.fd(fa)
 b.fd(fb)
 c.fd(fc)

 a.up()
 b.up()
 c.up()

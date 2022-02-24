import turtle
import random
from tkinter import *
from tkinter import colorchooser


a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()

color_code = {}
def choose_color(name):
    color_code['rgb'], color_code['hex'] = colorchooser.askcolor(title ="Choose the "+name+" color",color="")
    return color_code['hex']

def upThePens():
   a.up()
   b.up()
   c.up()
 
def downThePens():
   a.down()
   b.down()
   c.down()
def setPosition():
   a.setpos(random.randint(0,50),random.randint(0,50))
   b.setpos(random.randint(0,50),random.randint(0,50))
   c.setpos(random.randint(0,50),random.randint(0,50))

bg=turtle.Screen()
bg.bgcolor(choose_color("background"))

colors = [choose_color("first"), choose_color("second"),choose_color("third"), choose_color("fourth")]

a.hideturtle()
b.hideturtle()
c.hideturtle()

upThePens()

while(True):
 
   setPosition()
   downThePens()

   a.pensize(random.randint(1, 5))
   a.speed(random.randint(400000, 500000))
   a.color(random.choice(colors))

   b.pensize(random.randint(1, 5))
   b.speed(random.randint(400000, 500000))
   b.color(random.choice(colors))

   c.pensize(random.randint(1, 5))
   c.speed(random.randint(400000, 500000))
   c.color(random.choice(colors))

   if(random.randint(1, 50) % 2) == 0:
      a.rt(random.randint(45, 270))
      b.rt(random.randint(45, 270))
      c.rt(random.randint(45, 270))
   else:
      a.lt(random.randint(45, 270))
      a.circle(random.randint(200, 5000))
      b.lt(random.randint(45, 270))
      b.circle(random.randint(200, 5000))
      c.lt(random.randint(45, 270))
      c.circle(random.randint(200, 5000))

   fa = random.randint(25, 1000)
   fb = random.randint(25, 100)
   fc = random.randint(25, 100)

   a.fd(fa)
   b.fd(fb)
   c.fd(fc)
   
   upThePens()

import turtle as trl
import random
import tkinter as tk
from tkinter import colorchooser
from tkinter import simpledialog


a = trl.Turtle()
b = trl.Turtle()
c = trl.Turtle()

color_code = {}
pensize_num = {}
position_num = {}

def choose_color(name):
   color_code['rgb'], color_code['hex'] = colorchooser.askcolor(title ="Choose the "+name+" color",color="")
   return color_code['hex']

def input(passedTitle, text):
   dialog = tk.Tk()
   dialog.withdraw()
   userInput = simpledialog.askstring(title=passedTitle, prompt=text)
   return userInput

def upThePens():
   a.up()
   b.up()
   c.up()
 
def hideturtle():
   a.hideturtle()
   b.hideturtle()
   c.hideturtle()

def setPensize(first,second):
   a.pensize(random.randint(first, second))
   b.pensize(random.randint(first, second))
   c.pensize(random.randint(first, second))

def downThePens():
   a.down()
   b.down()
   c.down()

def setPosition(first,second,third,fourth):
   a.setpos(random.randint(first,second),random.randint(third,fourth))
   b.setpos(random.randint(first,second),random.randint(third,fourth))
   c.setpos(random.randint(first,second),random.randint(third,fourth))


hideturtle()

if input("RND","Did you want to randomize all?") == "no":
   pensize_num = [int(input("Pensize A", "Please define the end random number")), int(input("Pensize A", "Please define the end random number"))]
   position_num = [int(input("First rnd","Where the line need to START?")), int(input("Second rnd","Where the line need to START?")), int(input("First rnd","Where the line need to END?")), int(input("Second rnd","Where the line need to END?"))]
else:
   pensize_num = [5,10]
   position_num = [1,50,1,50]

bg=trl.Screen()
bg.bgcolor(choose_color("background"))

colors = [choose_color("first"), choose_color("second"),choose_color("third"), choose_color("fourth")]


upThePens()
while(True):
 
   setPosition(position_num[0], position_num[1], position_num[2], position_num[3])
   setPensize(pensize_num[0], pensize_num[1])
   downThePens()

   a.speed(random.randint(40, 50))
   a.color(random.choice(colors))
   b.speed(random.randint(40, 50))
   b.color(random.choice(colors))
   c.speed(random.randint(40, 50))
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

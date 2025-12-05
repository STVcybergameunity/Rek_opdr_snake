import random
import turtle as t
from turtle import *
import time
import tkinter as Tk



#visuals
bgcolor("black")
title("Snake")
delay(0)
setup(width=1.0, height=1.0)
Screen()
screen = t.Screen()

#name turtles
t=Turtle()
t1=Turtle()

#turtle display
t.showturtle()
t1.showturtle()
t.shape("turtle")
t1.shape("turtle")
t.width(15)
t1.width(15)
t.color("#ff33cc")
t1.color("#00ff00")
t.shapesize(1.5, 1.5, 3)
t1.shapesize(1.5, 1.5, 3)

#pen array
pen = []
pen1 = []

#move to start
t.penup()
t1.penup()
t.goto(750, 500)
t1.goto(-750,-400)
t.setheading(180)
t.pendown()
t1.pendown()

#player1 movement
def w():
    t.setheading(90)
def a():
    t.setheading(180)
def s():
    t.setheading(270)
def d():
    t.setheading(0)

onkey(w,'w')
onkey(s, 's')
onkey(a, 'a')
onkey(d, 'd')

#player2 movement
def up():
    t1.setheading(90)
def left():
    t1.setheading(180)
def down():
    t1.setheading(270)
def right():
    t1.setheading(0)

onkey(up,'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')

#hit detection
def hit(player, pen, pen1):
    x = player.xcor()
    y = player.ycor()

    #raken eigen pen

    for pos in pen:
        if abs(x - pos[0]) <15 and abs (y- pos[1]) <15:
            return True
        
    #ander pen raken
    for pos in pen1:
        if abs(x - pos[0]) <15 and abs (y - pos[1]) <15:
            return True
    # Buiten scherm
    if x < -screen.window_width()//2 or x > screen.window_width()//2 or \
       y < -screen.window_height()//2 or y > screen.window_height()//2:
        return True

    return False

def start():
    while True:
        pen.append((round (t.xcor()), round(t.ycor())))      
        pen1.append((round (t1.xcor()), round(t1.ycor())))

        t.stamp()
        t1.stamp()

        t.forward(20)
        t1.forward(20)
        
        #use hit detection
        if hit(pen, t, t1):
            print('Het spel is afgelopen')
            time.sleep(3)
            t.bye()
            
        if hit(pen1, t, t1):
            print('Het spel is afgelopen')
            time.sleep(3)
            t1.bye()

listen()
start()
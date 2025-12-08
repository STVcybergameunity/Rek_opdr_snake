import turtle as t
import time
from typing import Tuple, List

#create text writer
writer: t.Turtle = t.Turtle()
writer.hideturtle()
writer.penup()
writer.color("white")

#visuals
t.bgcolor("black")
t.title("Snake")
t.delay(0)
t.setup(width=1.0, height=1.0)
t.Screen()
screen = t.Screen()

#name turtles
player1: t.Turtle = t.Turtle()
player2: t.Turtle = t.Turtle()

#turtle display
player1.showturtle()
player2.showturtle()
player1.shape("turtle")
player2.shape("turtle")
player1.width(15)
player2.width(15)
player1.color("#ff33cc")
player2.color("#00ff00")
player1.shapesize(1.5, 1.5, 3)
player2.shapesize(1.5, 1.5, 3)

#pen array
pen: List[Tuple[int, int]] = []
pen1: List[Tuple[int, int]] = []

#move to start
player1.penup()
player2.penup()
player1.goto(740, 500)
player2.goto(-740, -400)
player1.setheading(180)
player2.setheading(0)
player1.pendown()
player2.pendown()

#player1 movement
def w() -> None:
    player1.setheading(90)
def a() -> None:
    player1.setheading(180)
def s() -> None:
    player1.setheading(270)
def d() -> None:
    player1.setheading(0)

t.onkey(w,'w')
t.onkey(s, 's')
t.onkey(a, 'a')
t.onkey(d, 'd')

#player2 movement
def up() -> None:
    player2.setheading(90)
def left() -> None:
    player2.setheading(180)
def down() -> None:
    player2.setheading(270)
def right() -> None:
    player2.setheading(0)

t.onkey(up,'Up')
t.onkey(down, 'Down')
t.onkey(left, 'Left')
t.onkey(right, 'Right')

#hit detection
def hit(player: t.Turtle, pen: List[Tuple[int, int]], pen1: List[Tuple[int, int]]) -> bool:
    x: float = player.xcor()
    y: float = player.ycor()

    #raken eigen pen

    for pos in pen:
        if abs(x - pos[0]) < 15 and abs(y - pos[1]) < 15:
            return True
        
    #ander pen raken
    for pos in pen1:
        if abs(x - pos[0]) < 15 and abs(y - pos[1]) < 15:
            return True
    # Buiten scherm
    if x < -screen.window_width()//2 or x > screen.window_width()//2 or \
       y < -screen.window_height()//2 or y > screen.window_height()//2:
        return True

    return False

def start() -> None:
    while True:
        pen.append((round (player1.xcor()), round(player1.ycor())))      
        pen1.append((round (player2.xcor()), round(player2.ycor())))

        player1.forward(20)
        player2.forward(20)
        
        time.sleep(0.1)
        
        #use hit detection
        if hit(player1, pen, pen1):
            writer.goto(0, 0)
            writer.write("Het spel is afgelopen", align="center", font=("Arial", 24, "normal"))
            time.sleep(3)
            writer.clear()
            reset_game()
            
        if hit(player2, pen, pen1):
            writer.goto(0, 0)
            writer.write("Het spel is afgelopen", align="center", font=("Arial", 24, "normal"))
            time.sleep(3)
            writer.clear()
            reset_game()

def reset_game() -> None:
    global pen, pen1
    pen.clear()
    pen1.clear()
    player1.goto(740, 500)
    player2.goto(-740, -400)
    player1.setheading(180)
    player2.setheading(0)
    player1.clear()
    player2.clear()

screen.listen()
start()

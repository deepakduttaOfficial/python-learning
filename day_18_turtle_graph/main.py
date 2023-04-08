from turtle import Turtle, Screen
from random import randint, choice

## Different way to import modules
## import turtle
## from turtle import Turtle
## from turtle import *
## import turtle as TURTLE

turtle = Turtle()
screen = Screen()
screen.colormode(255)
# <---------------- Draw a square challenge -------------------->
for _ in range(4):
    turtle.right(90)
    turtle.fd(100)

# <---------------- Draw a dash line challenge -------------------->
for _ in range(15):
    turtle.pendown()
    turtle.fd(10)
    turtle.penup()
    turtle.fd(10)

# <---------------- Trigonometric Drawing -------------------->
for i in range(3, 10):
    turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
    for _ in range(i):
        turtle.fd(100)
        turtle.right(360 / i)

# <---------------- random Drawing -------------------->
for _ in  range(50):
    screen.colormode(255)
    turtle.speed(10)
    turtle.pensize(10)
    turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
    if randint(0, 1) == 0:
        turtle.left(90)
    else:
        turtle.right(90) 
    turtle.fd(50) 
# <----------------------- another version ------------------>
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
turtle.pensize(15)
turtle.speed("fastest")

def random_color_gen():
    r = randint(0, 155)
    g = randint(0, 155)
    b = randint(0, 155)
    return (r, g, b)


for _ in range(200):
    turtle.color(random_color_gen())
    turtle.forward(30)
    turtle.setheading(choice(directions))

# <----------------------- Spirograph ------------------>
turtle.speed('fastest')
for _ in range(1, 72):
    turtle.pencolor(random_color_gen())
    turtle.circle(100)
    turtle.left(5)
# <----------------------- another version ------------------>
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color_gen())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)
draw_spirograph(5)


## Click to exit
screen.exitonclick()

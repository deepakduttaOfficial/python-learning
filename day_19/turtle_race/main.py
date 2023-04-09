
from turtle import Turtle, Screen
from random import randint
screen = Screen()

is_game_on = False
screen.setup(width=500, height=400)
chosen_turtle = screen.textinput(title='Make you bet', prompt='Choose you turtle')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtle = []

for i in range(6):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-230, -80 + i * 40)
    all_turtle.append(turtle)

if chosen_turtle:
    is_game_on = True

while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            wining_color = turtle.pencolor()
            print(wining_color)
            if wining_color == chosen_turtle:
                print(f"You've won! the {wining_color} turtle is winner")
            else:
                print(f"You've lost! the {wining_color} turtle is winner")
            is_game_on = False
        race_distance = randint(0, 10)
        turtle.forward(race_distance)

screen.exitonclick()
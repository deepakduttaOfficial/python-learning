from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()

def moveFd():
    turtle.fd(20)
    
def moveBw():
    turtle.backward(20)

def turnRight():
    turtle.right(10)

def turnLeft():
    turtle.left(10)

def clear():
    turtle.setpos(0,0)
    turtle.clear()

screen.onkeypress(moveFd, 'w')
screen.onkeypress(moveBw, 's')
screen.onkeypress(turnRight, 'a')
screen.onkeypress(turnLeft, 'd')
screen.onkeypress(clear, 'c')

screen.listen()
screen.exitonclick()


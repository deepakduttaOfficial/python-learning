## <----------------------- Final project hirst spot painting -------------------->
from turtle import Turtle, Screen
from random import choice
screen = Screen()
turtle = Turtle()
## colorgram USE FOR GET THE COLOR FOR IMAGE---------->
## from colorgram import extract
## rgb_colors = []
## colors = extract("./image.jpg", 2 ** 32)
## for color in colors:
##     r = color.rgb.r
##     g = color.rgb.g
##     b = color.rgb.b
##     new_color = (r,g,b)
##     rgb_colors.append(new_color)
## print(rgb_colors)
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

screen.colormode(255)
DEFAULT_POS = -180
turtle.penup()
turtle.hideturtle()
for i in range(1, 11):
    pos_change_vertically = DEFAULT_POS + (i * 30)
    turtle.setposition(DEFAULT_POS, pos_change_vertically)
    for n in range(1, 11):
        turtle.dot(15, choice(color_list))
        turtle.fd(30)



screen.exitonclick()
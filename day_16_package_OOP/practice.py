# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('red')
# timmy.forward(100)

# screen = Screen()
# screen.exitonclick()

# from turtle import Turtle, Screen
## ----------------------- PrettyTable ----------------------
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align['Type'] = "l"
print(table)

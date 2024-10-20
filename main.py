from turtle import Turtle, Screen
from prettytable import PrettyTable

# darry = Turtle()
# print(darry)
# darry.shape('turtle')
# darry.color('DarkOrange')
# darry.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])
print(table)
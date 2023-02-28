from turtle import Turtle, Screen
from prettytable import PrettyTable

# kamtu = Turtle()
# print (kamtu)
# def kamutu_star():
#     kamtu.shape("turtle")
#     kamtu.color("red")
#     kamtu.forward(150)
#     kamtu.right(150)
#     kamtu.forward(150)
#     kamtu.right(150)
#     kamtu.forward(150)
#     kamtu.right(150)
#     kamtu.forward(150)
#     kamtu.right(150)
#     kamtu.forward(150)
#     kamtu.right(150)
#     kamtu.forward(150)
#     kamtu.right(150)
#     kamtu.forward(150)
#     kamtu.right(150)
#     kamtu.forward(150)
#     kamtu.right(150)
#     kamtu.forward(150)
#     kamtu.right(150)
#     kamtu.forward(150)
#     kamtu.right(150)
#     kamtu.forward(150)
#     kamtu.right(150)
#     kamtu.forward(150)
#     kamtu.right(150)

# kamutu_star()
# kamtu.left(150)
# kamtu.forward(150)
# kamutu_star()

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'

print(table)
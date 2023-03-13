from turtle import Turtle
from food import Food

ALIGNMENT = 'center'
FONT = ("arial", 24, "normal")

# TODO 4: Create scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
            
    def count(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
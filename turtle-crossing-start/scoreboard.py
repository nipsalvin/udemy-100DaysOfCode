from turtle import Turtle

FONT = ("Courier", 24, "normal")

# TODO 3: Create and update scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)
    
    def next_level(self):
        self.level += 1
        self.update()
    
    def game_over(self):
        self.goto(0,0)
        self.penup()
        self.write("GAME OVER",align='center' , font=FONT)

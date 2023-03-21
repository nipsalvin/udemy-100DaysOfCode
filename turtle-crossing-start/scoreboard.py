from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update()
    
    def update(self):
        self.clear()
        self.goto(-250, 250)
        self.write(self.score, font=FONT)
    
    def next_level(self):
        self.score += 1
        self.update()
    
    def game_over(self):
        self.goto(-40,0)
        self.penup()
        self.write("GAME OVER", font=FONT)

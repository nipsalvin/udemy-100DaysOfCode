from turtle import Turtle
from food import Food

ALIGNMENT = 'center'
FONT = ("courier", 24, "normal")

# TODO 5: Create scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        """This creates the scoreboard as a turtle object"""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
            
    def count(self):
        """Adds 1 to the score anytime it is called"""
        self.score += 1
        if self.score >= self.highscore:
            self.highscore = self.score
        self.clear()
        self.write(f"Score: {self.score}, HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        """Prints GAME OVER once it is called"""
        self.goto(0,0)
        self.write("GAME OVER", align="center", font= FONT )
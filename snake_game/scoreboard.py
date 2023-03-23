from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("courier", 24, "normal")

# TODO 5: Create scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        """This creates the scoreboard as a turtle object"""
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()
            
    def update_scoreboard(self):
        """This function updates the score board"""
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """This resets the score to 0 and calls update_scoreboard()"""
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    

            
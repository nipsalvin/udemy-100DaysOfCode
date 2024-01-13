from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()
    
    def update_scoreboard(self):
        '''This DISPLAYS the scores(points) gained and the lives remaining'''
        self.clear()
        self.goto(x=-200, y=350)
        self.write(f'Scores: {self.score}')
        self.goto(x=180, y=350)
        self.write(f'Lives: {self.lives +1}')

    def update_lives(self):
        '''This keeps track of the lives remaining'''
        self.lives -= 1
        self.update_scoreboard()
    
    def update_points(self):
        '''This keeps track of the points gained'''
        self.score += 1
        self.update_scoreboard()
    
    def gameover(self):
        self.goto(0,0)
        self.write('GAME OVER', align='center', font=('courier', 30, 'bold'))
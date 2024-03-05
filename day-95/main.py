from turtle import Screen, Turtle
import random

"""Constants"""
SHIP_MOVEMENT = 20
LASER_MOVEMENT = 45
ALIEN_SPEED = 3

"""Screen"""
screen = Screen()
screen.title("Space Invaders")
screen.bgcolor('black')
screen.screensize(600, 600)
screen.setup(650, 850)

"""Ship"""
ship = Turtle('arrow')
ship.penup()
ship.speed(0)
ship.setposition(0, -350)
ship.color('pink')
ship.left(90)
ship.shapesize(stretch_wid=1, stretch_len=2)

"""Enemies"""
all_enemies = []
number_of_enemies = random.randint(5, 15)
for _ in range(number_of_enemies):
    all_enemies.append(Turtle('turtle'))
for enemy in all_enemies:
    enemy.penup()
    enemy.color('red')
    enemy.speed(0)
    enemy.setheading(270)
    x = random.randint(-250, 250)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

"""Functions"""
def move_left():
    x = ship.xcor()
    y = ship.ycor()
    ship.goto(x - SHIP_MOVEMENT, y)

def move_right():
    laser.showturtle()
    x = ship.xcor()
    y = ship.ycor()
    ship.goto(x + SHIP_MOVEMENT, y)

def fire():
    global laser_state
    if laser_state == 'ready':
        laser_state = 'fire'
        x = ship.xcor()
        y = ship.ycor() + 10
        laser.setposition(x, y)
        laser.showturtle()

"""Functionality"""
screen.listen()
screen.onkey(move_left, 'Left')
screen.onkey(move_right, 'Right')
screen.onkey(fire, 'space')

"""Laser beam"""
laser = Turtle()
laser.color('white')
laser.penup()
laser.shape('square')
laser.shapesize(stretch_len=0.8, stretch_wid=0.4)
laser.left(90)
laser.speed(0)
laser.hideturtle()
laser_state = 'ready'

"""Scoreboard"""
score = 0
score_label = Turtle()
score_label.speed(0)
score_label.penup()
score_label.color('white')
score_label.setposition(-280, 285)
score_label.hideturtle()
score_label.write(f'Score: {score}', align='left', font=('Arial', 20, 'normal'))
with open("high_score.txt") as data:
    high_score = int(data.read())

"""Game loop"""
while True:
    screen.update()
    for enemy in all_enemies:
        x = enemy.xcor()
        x += ALIEN_SPEED
        enemy.setx(x)
        if enemy.xcor() > 300:
            for e in all_enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)   
            ALIEN_SPEED *= -1
        if enemy.xcor() < -300:
            for e in all_enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            ALIEN_SPEED *= -1
        if laser.distance(enemy) < 20:
            laser.hideturtle()
            laser_state = 'ready'
            laser.setposition(0, -340)
            x = random.randint(-250, 250)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            score += 10
            score_label.clear()
            score_label.write(f'Score: {score}', font=('Arial', 20, 'normal'))
            if score > high_score:
                high_score = score
                with open('high_score.txt', mode='w') as data:
                    data.write(f'{high_score}')
        if ship.distance(enemy) < 20:
            ship.hideturtle()
            enemy.hideturtle()
            print('Game Over')
            game_over = Turtle()
            game_over.speed(0)
            game_over.color('red')
            game_over.penup()
            game_over.hideturtle()
            game_over.setposition(0, 0)
            game_over.write('GAME OVER', align='center', font=('Arial', 30, 'normal'))

            message = f'Your score was {score}. Highest score is {high_score}'
            game_over_message = Turtle()
            game_over_message.speed(0)
            game_over_message.color('white')
            game_over_message.penup()
            game_over_message.hideturtle()
            game_over_message.setposition(0, -50)
            game_over_message.write(f'{message}', align='center', font=('Arial', 15, 'normal'))

            break
        if enemy.ycor() <= ship.ycor():
            ship.hideturtle()
            enemy.hideturtle()
            print('Game Over')
            game_over = Turtle()
            game_over.speed(0)
            game_over.color('red')
            game_over.penup()
            game_over.hideturtle()
            game_over.setposition(0, 0)
            game_over.write('GAME OVER', align='center', font=('Arial', 30, 'normal'))

            message = f'Your score was {score}. Highest score is {high_score}'
            game_over_message = Turtle()
            game_over_message.speed(0)
            game_over_message.color('white')
            game_over_message.penup()
            game_over_message.hideturtle()
            game_over_message.setposition(0, -50)
            game_over_message.write(f'{message}', align='center', font=('Arial', 15, 'normal'))
            

            break
    if laser_state == 'fire':
        y = laser.ycor()
        y += LASER_MOVEMENT
        laser.sety(y)
    if laser.ycor() > 270:
        laser.hideturtle()
        laser_state = 'ready'
        laser.setposition(0, -340)

# TODO: Add gameover functionality
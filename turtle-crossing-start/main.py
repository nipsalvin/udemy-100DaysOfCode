import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # TODO 3: Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False

    # TODO 4: Detect crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()


screen.exitonclick()


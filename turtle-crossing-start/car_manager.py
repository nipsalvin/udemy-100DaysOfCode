from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3

# TODO 2: Create and Move Car 
class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 5:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            y_position = random.randint(-250, 250)
            new_car.goto(280, y_position)
            new_car.setheading(180)
            self.all_cars.append(new_car)
    
    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
        
    def level_up(self):
        self.car_speed += MOVE_INCREMENT


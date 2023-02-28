class User:
    def __init__(self):
        print("User is being created")
    
user = User()
user.name = "Alvin"
user.age = 28

class Car:
    def __init__(self, seats, wheels):
        self.seats = seats
        self.wheels = wheels
        print("Car is being created")

my_car = Car(5, 4)
print(f'my car has {my_car.seats} seats')

his_car = Car(4, 4)   
print(f'his car has {his_car.seats} seats')    
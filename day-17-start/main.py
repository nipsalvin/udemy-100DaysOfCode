class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.followers = 0
        self.following = 0
        print("User is being created")
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

    
user_1 = User("xxx",28)
# print(user_1.followers)
user_2 = User("yyy", 29)
user_1.follow(user_2)

print(f'{user_1.name} has {user_1.followers} followers')
print(f'{user_1.name} is following {user_1.following} people')
print(f'{user_2.name} has {user_2.followers} followers')
print(f'{user_2.name} is following {user_2.following} people')

class Car:
    def __init__(self, seats, wheels):
        self.seats = seats
        self.wheels = wheels
        print("Car is being created")

my_car = Car(5, 4)
print(f'my car has {my_car.seats} seats')

his_car = Car(4, 4)   
print(f'his car has {his_car.seats} seats')    

her_car_seats = int(input("How many car seats?\n"))
her_car_wheels = int(input("How many wheels?\n"))
her_car = Car(her_car_seats, her_car_wheels)
print(f'Her car has {her_car.seats} seats') 
print(f'Her car has {her_car.wheels} wheels')
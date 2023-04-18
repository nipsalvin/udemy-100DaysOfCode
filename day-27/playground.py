def add(*args):
    sum = 0 
    for n in args:
        # print(n)
        sum += n
    print(type(args))
    return sum

print(add(3, 4, 5))

def calc(n, **kwargs):
    print(n)
    n -= kwargs['minus']
    print(n)
    n *= kwargs['multiply']
    print(n)

calc(8, minus = 3, multiply = 5)


class Car:
    def __init__(self, **kw) :
        self.make = kw['make']
        self.model = kw['model']

        """Method 2 to call values from keys in a dict is"""
        """Returns non if no Value is assigned to Key"""
        self.seats = kw.get('seats')
        self.fwd = kw.get('fwd')
        self.country = kw.get('country')
        self.speed = kw.get('speed')
    
my_car = Car(make = 'Nissan', model = 'GTR', seats = 5, speed = 6)
print(my_car.make, my_car.speed)



'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''
class Car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed
    def speed(self):
        self.max_speed += 5
        return self.max_speed
    def details(self, model, year, max_speed):
        print(model, year, max_speed)
        return ' '

tesla = Car('Tesla', 2020, 180)
print(tesla.details('Tesla', 2020, tesla.speed()))
bmw = Car('BMW i8', 2019, 210)
print(bmw.details('BMW i8', 2019, bmw.speed()))
'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return float(self.length * self.width)
    def perimeter(self):
        self.length += self.length
        self.width += self.width
        return float(self.length + self.width)

class circle_:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        self.radius *= self.radius
        return 3.14 * self.radius
    def circum(self):
        self.radius *= 2
        return 3.14 * self.radius

rect = rectangle(50, 25)
print("This is the rectangles area: " ,rect.area())
print("This is the rectangles perimeter: " ,rect.perimeter())
circle = circle_(10)
print("This is the circles area: " ,circle.area())
print("This is the circles circumference: " ,circle.circum())
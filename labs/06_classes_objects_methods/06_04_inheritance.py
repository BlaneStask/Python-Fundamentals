'''
Build on the previous exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercise.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''
class fruit:
    def __init__(self, name, cost = 2, amount = 3):
        self.name = name
        self.cost = cost
        self.amount = amount
    def __str__(self):
        return self.cost + 5
    def print_(self, name, cost = 2, amount = 3):
        print(name, cost, amount)
        return '\n'

class vegetable:
    def __init__(self, name, cost = 5, amount = 4):
        self.name = name
        self.cost = cost
        self.amount = amount
    def __str__(self):
        return self.amount + self.cost
    def print_(self, name, cost = 5, amount = 4):
        print(name, cost, amount)
        return '\n'

class meat:
    def __init__(self, name, cost = 10, amount = 2):
        self.name = name
        self.cost = cost
        self.amount = amount
    def __str__(self):
        return self.cost - (self.cost / 2)
    def print_(self, name, cost = 10, amount = 2):
        print(name, cost, amount)
        return '\n'

class plants(vegetable):
    def print_(self, name, cost=2, amount=4):
            print(name, cost, amount)
            return '\n'

class animals(meat):
    def print_(self, name, cost=500, amount=490):
            print(name, cost, amount)
            return '\n'

apple = fruit('Apple', 10, 7)
print("The name, cost and amount for the item(s) of food are:")
print(apple.print_('Apple', 10, 7))
print("After June 15th the price for Apples will be increased by $5:")
print(apple.__str__() ,'\n')
print("The name, cost and amount for the item(s) of food are:")
carrot = vegetable('Carrot', 5)
print(carrot.print_('Carrot', 5))
print("Here take more vegetables:")
print(carrot.__str__() ,'\n')
print("The name, cost and amount for the item(s) of food are:")
chicken = meat('Chicken', 12, 5)
print(chicken.print_('Chicken', 12, 5))
print("During the weekend all meat products are 50% off:")
print(chicken.__str__() ,'\n')
banana = fruit('Banana', 4, 6)
print("The name, cost and amount for the item(s) of food are:")
print(banana.print_('Banana', 4, 6))
print("After June 15th all fruit products will be increased by $5:")
print(banana.__str__() ,'\n')
print("The name, cost and amount for the item(s) of food are:")
okra = vegetable('Okra', 3, 7)
print(okra.print_('Okra', 3, 7))
print("Here take more vegetables:")
print(okra.__str__() ,'\n')
print("The name, cost and amount for the item(s) of food are:")
veal = meat('Veal', 13)
print(veal.print_('Veal', 13))
print("During the weekend all meat products are 50% off:")
print(veal.__str__() ,'\n')
plant = plants('Beets', 2, 11)
print("The name, cost and amount of vegetables from a plant are:")
print(plant.print_('Beets', 2, 11) ,'\n')
cow = animals('Cow', 500, 400)
print("The name, cost and amount of meat gained from an animal are:")
print(cow.print_('Cow', 500, 400))
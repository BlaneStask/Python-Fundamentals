'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


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
print(veal.__str__())
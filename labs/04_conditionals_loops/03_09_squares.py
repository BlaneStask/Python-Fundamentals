'''
Write a script that prints out all the squares of numbers from 1- 50

Use a for loop that demonstrates the use of the range function.

'''
def squares():
    l = list()
    for i in range(1, 50):
        l.append(i ** 2)
    print(l)

squares()


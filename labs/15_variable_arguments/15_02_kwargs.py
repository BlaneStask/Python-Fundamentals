'''
Write a script with a function that demonstrates the use of **kwargs.

'''


def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


my_function(Ben='hi', Bill='hello')

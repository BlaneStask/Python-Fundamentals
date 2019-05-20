'''
Write a decorator function that wraps text passed to it in a specified html tag.
The user should be able to decide which tag to use.

'''


def decorator_func(initial_func):
    def wrapper_func():
        your_input = input("Type your own tag: ")
        return initial_func()
    return wrapper_func


@decorator_func
def dec():
    print("What a good idea!")


dec()

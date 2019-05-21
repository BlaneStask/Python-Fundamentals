'''
Write a lambda function that does not take in an arguments but returns a value. Print the return value.

'''
value = lambda *args, **kwargs: None

print("The return value is: ", value())

'''
Write a script that demonstrates a try/except/else.

'''
try:
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))
    z = x / y
    print("The division of the two values are: ", z)
except ZeroDivisionError:
    print("You cannot divide by zero: ZeroDivisionError")
except ValueError:
    print("You cannot divide by a non-integer value: ValueError")
else:
    print("Thanks for entering the proper values for division!")

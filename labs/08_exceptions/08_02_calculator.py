'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

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
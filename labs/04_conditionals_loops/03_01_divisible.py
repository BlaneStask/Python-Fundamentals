'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
number = input("Give me a number between 1 and 1,000,000,000: ")
num = int(number)

if num < 1 and num > 1000000000:
    print(num, " is not in the proper range.")
elif (num / 3) != float:
    res = num / 3
    print(num," is divisible by 3 and the result is: ",res)
else:
    print(num, " is not divisible by 3")
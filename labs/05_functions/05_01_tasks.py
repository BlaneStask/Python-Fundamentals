'''

Write a script that completes the following tasks.

'''


# takes in a number from the user between 1 and 1,000,000,000

# calls a function that determines whether the number is divisible by both 4 and 7

# calls a function that determines whether the number is divisible by 4 or 7

# calls a function that determines whether the number is divisible by 4 or 7 exclusively

# print the results

number = input("Enter a value from 1 and 1,000,000,000: ")
num = int(number)
x = num % 4
y = num % 7

def div(num):

    if x == 0 and y == 0:
        print("This value is divisible by 4 and 7.")
    elif x == 0:
        print("This value is divisible by 4.")
    elif y == 0:
        print("This value is divisible by 7.")
    else:
        print("This value is not divisible by 4 or 7.")

div(sum)
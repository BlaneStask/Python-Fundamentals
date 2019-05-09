'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
number = input("Give me a number from 0 and 1,000,000,000: ")
num = int(number)

counter = 0

while counter <= num:
    if counter == num:
        print(num)
        break
    else:
        counter += 1
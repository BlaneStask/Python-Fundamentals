'''
Write a lambda function that takes in 3 numbers and returns the sum of the numbers.

'''
numbers = input("Enter three numbers, separated my a space: ")

num_sum = lambda x: sum(int(x) for x in numbers if x.isdigit())

print("The sum of the values in the list are: ", num_sum(numbers))

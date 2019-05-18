'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''
input_string = input("Enter a list of values separated by a space: ")

def sum_digits(digit):
    return sum(int(x) for x in digit if x.isdigit())

print("The sum of the values in the list are: ", sum_digits(input_string))

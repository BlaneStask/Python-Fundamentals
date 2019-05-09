'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''
low = input("Give me the lower bound: ")
m = int(low)
upper = input("Give me the upper bound: ")
n = int(upper)

sum = 0

for i in range (m,n+1):
    sum += i

print(sum)
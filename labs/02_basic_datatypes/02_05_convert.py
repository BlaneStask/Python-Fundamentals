'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
#1)
x = 10
y = 6
conv = float(x) * y
print(conv)
#2)
print(int(conv))
#3)
z = 11.4
conv = float(x) * y
floor_d = conv // z
print(floor_d)
#4)
user_input = int(input("Gimme the first value: "))
v_one = int(user_input)
user_input2 = int(input("Gimme the second value: "))
v_two = int(user_input2)
multi = v_one * v_two
print(multi)
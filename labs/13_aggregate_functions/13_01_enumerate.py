'''
Demonstrate the use of the .enumerate() function.
'''
my_list = ["apple", "banana", "orange"]

for index, obj1 in enumerate(my_list):
    print(f"({index}, '{obj1}')", end="")

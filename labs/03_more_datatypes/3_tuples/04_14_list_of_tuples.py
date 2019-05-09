'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

string = input("Write a sentence: ")

tuple1 = tuple(string)

list1 = [tuple1]

print("The list after conversion to tuple list: " ,list1)

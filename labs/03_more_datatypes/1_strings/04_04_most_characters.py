'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''
string = input("Type a sentence: ")

string1 = input("Type another sentence: ")

string2 = input("Type another sentence: ")

a = string
b = string1
c = string2

if len(a) > len(c) and len(a) > len(b):
    print("The first sentence has the most characters.")
elif len(b) > len(a) and len(b) > len(c):
    print("The second sentence has the most characters.")
else:
    print("The third sentence has the most characters.")
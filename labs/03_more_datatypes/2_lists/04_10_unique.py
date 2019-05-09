'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list1 = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

print("list: ",list1)
my_set = set(list1)
my_new_list = list(my_set)

print("unique_list: ",my_new_list)
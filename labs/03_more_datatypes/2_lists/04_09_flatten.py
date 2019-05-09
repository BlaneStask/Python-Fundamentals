'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

flatten = []
for sublist in list:
    for item in sublist:
        flatten.append(item)

print(flatten)
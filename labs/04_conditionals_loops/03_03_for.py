'''
Using a "for-loop", print out all odd numbers from 1-100.

'''
start, end = 0, 99

for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=" ")
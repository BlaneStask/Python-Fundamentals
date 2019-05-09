'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
str = input("Give me a list of words with duplicates: ")

def freq(str):
    str_list = str.split()
    unique_words = set(str_list)
    for words in unique_words:
        print('Frequency of ', words, 'is :', str_list.count(words))

if __name__ == "__main__":
    freq(str)
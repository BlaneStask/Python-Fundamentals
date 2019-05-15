'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
with open("words.txt", "r") as fin:

    def short():
        for item in fin:
            l = item.split()
            return(min(l, key=len))

    print("The shortest word(s) is: " '\n')
    print(short() ,'\n')

    def long(p):
        s = 0
        for item in fin:
            if len(item) >= p:
                s =[item]
                p = len(item)
        return s

    print("The longest word(s) is: " '\n')
    print("[' ']" .join(long(0)),'\n')

    def total(num_words):
        for line in fin:
            words = line.split()
            num_words += len(words)
        return num_words

    print("Number of words:" '\n')
    print(total(0))
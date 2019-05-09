'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''
string = input("Type out a sentence: ")
symbol = input("Give a symbol: ")

def change(string):
  char = string[0]
  string = string.replace(char, symbol)

  return string

print(change(string))
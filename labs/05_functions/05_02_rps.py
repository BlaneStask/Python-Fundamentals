'''
Code a game of rock paper scissors.

'''
def get_hand(hand):
    scissors = 0
    rock = 1
    paper = 2
    if hand == 0:
        print("Your hand is scissors, good luck!")
        return scissors
    elif hand == 1:
        print("Your hand is rock, good luck!")
        return rock
    else:
        print("Your hand is paper, good luck!")
        return paper

def get_comp(computer):
    scissors = 0
    rock = 1
    paper = 2
    if computer == 0:
        print("The computer has scissors!")
        return scissors
    elif computer == 1:
        print("The computer has rock!")
        return rock
    else:
        print("The computer has paper!")
        return paper


def determine_winner(computer, player):
    if computer == player:
        print("You tied!")
    elif computer == 2 and player != 0:
        print("You lost :(")
    elif computer == 1 and player != 2:
        print("You lost :(")
    elif computer == 0 and player != 1:
        print("You lost :(")
    else:
        print("You won!")

number = input("Give me a number from 0 to 2 to represent your hand. 0 = scissor, 1 = rock, 2 = paper: ")
hand = int(number)

import random
computer = random.randint(0, 2)

get_hand(hand)
get_comp(computer)

determine_winner(computer,hand)
# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random


def rolling_a_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1,6)
    sum = dice1 + dice2
    print("The sum of the dice is {} + {} = {}".format(dice1, dice2, sum))
    return sum

def playing_a_game():
    rolling = rolling_a_dice()
    if rolling == 7 or rolling == 11:
        print("You won")
        return True

    elif rolling == 2 or rolling == 3 or rolling == 12:
        print ("You lose")
        return False

    else:
        print("Now your goal number is {}".format(rolling))
        goal = rolling
        while True:
            rolling = rolling_a_dice()
            if rolling == goal:
                print("You are a winner!")
                return True
            elif rolling == 7:
                print ("You lose!")
                return False
            else:
                print("Please roll again.")

playing_a_game()








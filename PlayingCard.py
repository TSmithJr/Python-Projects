# PlayingCard.py


"""
MIS 15-01

This program takes user input describing a
playing card in shorthand, and then displays
the full description of the card. If a user
inputs an invalid card such as "00", it will
notify the user.
"""


def main():  # define main

    # get user input for card notation
    card = input("Enter the card notation: ").upper()

    # create strings for the 1st and 2nd card words
    wordOne = ""
    wordTwo = ""

    # index the user string, the variable "type" indexes the first character
    cardType = card[0]
    # index the user string, similar to type, from the 2nd character to the end of string
    cardFamily = card[1:]
    # indexes the first two string values to check if the card type is ten
    tenCheck = card[0:2]

    # if and else if statements to see what the card type is
    if cardType == "A":
        wordOne = "Ace of "
    elif cardType == "J":
        wordOne = "Jack of "
    elif cardType == "Q":
        wordOne = "Queen of "
    elif cardType == "K":
        wordOne = "King of "
    elif cardType == "2":
        wordOne = "Two of "
    elif cardType == "3":
        wordOne = "Three of "
    elif cardType == "4":
        wordOne = "Four of "
    elif cardType == "5":
        wordOne = "Five of "
    elif cardType == "6":
        wordOne = "Six of "
    elif cardType == "7":
        wordOne = "Seven of "
    elif cardType == "8":
        wordOne = "Eight of "
    elif cardType == "9":
        wordOne = "Nine of "
    elif tenCheck == "10":
        wordOne = "Ten of "
    # else statement to check for invalid values, and exit the program safely
    else:
        print("Your selection is Invalid"), exit()

    # if and else if statements to see what the card family is
    # or statements to account for the card type being "10"
    if cardFamily == "D" or cardFamily == "0D":
        wordTwo = "Diamonds"
    elif cardFamily == "H" or cardFamily == "0H":
        wordTwo = "Hearts"
    elif cardFamily == "S" or cardFamily == "0S":
        wordTwo = "Spades"
    elif cardFamily == "C" or cardFamily == "0C":
        wordTwo = "Clubs"
    # else statement to check for invalid values, and exit the program safely
    else:
        print("Your selection is Invalid"), exit()

    # printing the full, descriptive strings in place of shorthanded user input
    print("You selected " "\"" + wordOne + wordTwo + "\" "), print("\n"), main()


main()  # call main

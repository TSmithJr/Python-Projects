# CreditCard.py

"""
MIS15

Credit card
"""


def isValid(card_number):
    # Return true if card number is valid

    # See if the card is a digit
    if not card_number.isdigit():
        return False

    # Call get size to see if card has a valid length
    if getSize(card_number) not in [13, 14, 15, 16]:
        return False

    # Assign d so prefix function can run
    d = 0
    if not prefixMatched(card_number, d):
        return False

    sum_of_even = sumOfDoubleEvenPlace(card_number)
    sum_of_odd = sumOfOddPlace(card_number)
    sum_even_odd = sum_of_even + sum_of_odd

    if sum_even_odd % 10 == 0:
        return True

    return False


def sumOfDoubleEvenPlace(card_number):
    # Sum of steps 1 and 2
    output = 0

    for i in range(len(card_number) - 2, -1, -2):
        num = int(card_number[i]) * 2
        num = getDigit(num)
        output += num

    return output


def getDigit(number):
    # Return this number if it is a single digit,
    # otherwise, return the sum of the two digits
    if number > 9:
        number = int(str(number)[0]) + int(str(number)[1])

    return number


def sumOfOddPlace(card_number):
    # Return sum of odd place digits in card number
    output = 0
    for i in range(len(card_number) - 1, -1, -2):
        num = int(card_number[i])
        output += num

    return output


def prefixMatched(card_number, d):
    # Return true if the digit d is a prefix for
    # card number (d = 4,5,6, or 37)
    if card_number[:1] == "4":
        d = 4
    elif card_number[:1] == "5":
        d = 5
    elif card_number[:1] == "6":
        d = 6
    elif card_number[:2] == "37":
        d = 37
    else:
        return False

    if d == 4 or d == 5 or d == 6 or d == 37:
        return True


def getSize(card_number):
    # Return the number of digits in card_number
    output = len(card_number)

    return output


def cardType(card_number):
    #Determine type of card
    if card_number[:1] == "4":
        return "Visa"
    elif card_number[:1] == "5":
        return "Mastercard"
    elif card_number[:1] == "6":
        return "Discover"
    elif card_number[:2] == "37":
        return "American Express"
    else:
        return False


def main():
    #Get input
    card_number = input("Enter your credit card number: ")
    #Call cardType
    card_type = cardType(card_number)

    #print statement in loop until valid number is entered
    if isValid(card_number):
        print("Your card is: " + str(card_type))
        print(str(card_number) + " is valid.")
    else:
        print("Invalid card number.")
        main()

main()

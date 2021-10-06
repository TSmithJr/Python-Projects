# StringOperation.py

"""
MIS15

Takes a user string and outputs
uppercase letters, every third letter,
all vowels replaced by _'s, the number
of digits, and the position of vowels.
"""


# Validates user input
def stringValidation():
    string = input("Enter a string:\n")

    # data validation for numeric
    if string.isnumeric():
        print("Invalid input"), exit()

    return string


# Prints uppercase letter in string
def uppercaseString(string):
    upperString = [x for x in string if x.isupper()]
    print("\t1) Upper case letters")
    print("\t   " + "".join(upperString) + "\n")


# Prints every third letter of string
def everyThirdLetter(string):
    thirdString = ""
    for i in range(2, len(string), 3):
        thirdString += string[i]
    print("\t2) Every third letter")
    print("\t   " + thirdString + "\n")


# Replaces each vowel in string with an underscore
def vowelsToUnderscore(string):
    vowelUndrString = string
    vowels = 'aeiouAEIOU'
    for x in string:
        if x in vowels:
            vowelUndrString = vowelUndrString.replace(x, "_")
    print("\t3) All vowels replaced by underscores")
    print("\t   " + vowelUndrString + "\n")


# Shows number of digits in string
def digitsInString(string):
    digitString = 0
    digits = '0123456789'
    for i in string:
        if i in digits:
            digitString += 1
    print("\t4) Number of digits")
    print("\t  ", digitString, "digits", "\n")


# Shows numerical position of vowels in string
def vowelPosition(string):
    vowelPosString = 0
    vowels = 'aeiouAEIOU'
    outputList = []
    print("\t5) Positions of vowels")
    for i in string:
        if i in vowels:
            outputList.append(str(vowelPosString))
        vowelPosString += 1
    print("\t   " + " ".join(outputList))


def main():
    # Validated assignment
    string = stringValidation()

    # Print output for formatting
    print("\nOutput:")

    # Call each function for validated string
    uppercaseString(string)
    everyThirdLetter(string)
    vowelsToUnderscore(string)
    digitsInString(string)
    vowelPosition(string)


main()  # Call main

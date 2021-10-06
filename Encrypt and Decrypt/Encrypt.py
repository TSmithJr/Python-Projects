# Encrypt.py

"""
MIS 15 Group 3
Dany, Logan, Timmy Troy
"""


def encryptText(text, userInput):
    # Declare variable for final string output
    final = ""

    for i in range(len(text)):
        letter = text[i]
        if letter.isalpha():
            if letter.isupper():
                # Formula to account for uppercase letters
                final += chr((ord(letter) + userInput - 65) % 26 + 65)
            else:
                # Formula to account for lowercase letters
                final += chr((ord(letter) + userInput - 97) % 26 + 97)
        else:
            final += letter

    return final


def main():
    userInput = input("Enter encryption/decryption key: ")

    try:
        val = int(userInput)
    except ValueError:
        print("Invalid input"), exit()

    userInput = int(userInput)
    if userInput > 25:
        print("Invalid input"), exit()
    elif userInput < 1:
        print("Invalid input"), exit()

    try:
        file_in = open("Email.txt", "r")
        file_out = open("EncryptedEmail.txt", "w")
        for text in file_in:
            file_out.write(encryptText(text, userInput))

        print("Encryption successful with key", userInput)
    except FileNotFoundError:
        print("File not found, please provide a file and try again"), exit()


main()

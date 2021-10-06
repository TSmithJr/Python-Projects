# Decrypt.py

"""
MIS 15
"""


def decryptText(text, userInput):
    final = ""

    for i in range(len(text)):
        letter = text[i]

        if letter.isalpha():
            if letter.isupper():
                final += chr((ord(letter) - userInput - 65) % 26 + 65)
            else:
                final += chr((ord(letter) - userInput - 97) % 26 + 97)
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
        file_in = open("EncryptedEmail.txt", "r")
        encrypt = file_in.read()
        print("\nEncrypted file contents: ")
        print(encrypt)

        file_in2 = open("EncryptedEmail.txt", "r")
        file_out = open("DecryptedEmail.txt", "w")
        for text in file_in2:
            file_out.write(decryptText(text, userInput))
        file_out.close()
        file_in2.close()

        file_final = open("DecryptedEmail.txt", "r")
        decrypt = file_final.read()
        print("\nDecrypted file contents: ")
        print(decrypt)
    except FileNotFoundError:
        print("File not found, please provide a file and try again"), exit()


main()

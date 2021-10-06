# Week.py

"""
MIS15

This program prints the day of the week for any
given date in the Gregorian calendar. User input
is required for the original date.
"""


# Data validation for date
def getDate():

    # Declare variables for m, d, y
    month = "0"
    day = "0"
    year = "0"

    # Prompt for user input
    date = input("Enter a date in mm/dd/yyyy format: ")

    # For loop to count number of slashes in date
    count = 0
    for i in date:
        if i == "/":
            count += 1

    # Data validation checks for date string
    if date.isalpha():
        print("Invalid date"), exit()
    if date.isalnum():
        print("Invalid date"), exit()
    if count < 2 or count >= 3:
        print("Invalid date"), exit()
    if len(date) < 8 or len(date) > 10:
        print("Invalid date"), exit()

    # Split date into variables after validated
    month, day, year = date.split("/")

    # Validate m, d, y to make sure they have a value
    if len(month) == 0:
        print("Invalid date"), exit()
    if len(day) == 0:
        print("Invalid date"), exit()
    if len(year) == 0:
        print("Invalid date"), exit()

    # Declare integers
    month = int(month)
    day = int(day)
    year = int(year)

    # Valid month, day, and leap year check
    if month > 12 or month < 1:
        print("Invalid date"), exit()
    if day > 31 or day < 1:
        print("Invalid date"), exit()
    if month == 2 and day >= 29 and (year % 4) != 0:
        print("Invalid date"), exit()

    return date


# Data Validation for negative date
def negativeDate(month, day, year):
    if month <= 0 or month >= 13 or day <= 0 or day >= 31 or year < 1000:
        print("Invalid date"), exit()


# Leap year check as per instructions
def leapYear(month, year):
    if year % 4 == 0 and month in (1, 2):
        return -1


def main():
    # Declare all variables
    formulaMain = 0
    centuryCode = 0
    keyValue = 0

    # Assign date after it has been validated
    date = getDate()

    # use split function to get variables
    month, day, year = date.split("/")
    month = int(month)
    day = int(day)
    year = int(year)

    # Negative validation for date
    negativeDate(month, day, year)

    # Get last two digits of year
    year = str(year)
    lastTwo = year[2:4]
    lastTwo = int(lastTwo)

    # Assign key value for each month using dictionary function
    month = str(month)
    monthDict = {"1": 1, "2": 4, "3": 4, "4": 0, "5": 2, "6": 5,
                 "7": 0, "8": 3, "9": 6, "10": 1, "11": 4, "12": 6, }
    if month in monthDict:
        keyValue = monthDict[month]

    # While statements to make it possible to get a century code
    year = int(year)
    while year > 2099:
        year -= 400
    while year < 1700:
        year += 400

    # Calculates which century for main formula
    if 1700 <= year <= 1799:
        centuryCode = 4
    elif 1800 <= year <= 1899:
        centuryCode = 2
    elif 1900 <= year <= 1999:
        centuryCode = 0
    elif 2000 <= year <= 2099:
        centuryCode = 6

    # Adds up values before leap year check
    formulaMain = (lastTwo // 4) + day + keyValue + centuryCode

    # Leap year check, subtracts one according to instructions
    year = int(year)
    month = int(month)
    if leapYear(month, year) == -1:
        formulaMain -= 1

    # Adds last two digits to formula, takes remainder by 7
    formulaMain += lastTwo
    formulaMain = formulaMain % 7

    # conditionals for which day of the week the date is
    if formulaMain == 1:
        print("Day of the week is Sunday")
    elif formulaMain == 2:
        print("Day of the week is Monday")
    elif formulaMain == 3:
        print("Day of the week is Tuesday")
    elif formulaMain == 4:
        print("Day of the week is Wednesday")
    elif formulaMain == 5:
        print("Day of the week is Thursday")
    elif formulaMain == 6:
        print("Day of the week is Friday")
    elif formulaMain == 7 or formulaMain == 0:
        print("Day of the week is Saturday")

    # validation check for days of the week
    if formulaMain > 7:
        print("Invalid date")


main()  # Call main

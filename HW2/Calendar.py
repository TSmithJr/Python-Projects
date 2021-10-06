# Calendar.py

"""
MIS15

This programs prints a full month calendar
when the user provides the month and the
year.
"""

import calendar


# Data validation for month
def monthCheck():
    month = input("Enter month\n(1-Jan, 2-Feb, 3-Mar, 4-Apr, 5-May," +
                  "6-Jun,\n7-Jul, 8-Aug, 9-Sep, 10-Oct, 11-Nov, 12-Dec): ")

    if not month.isdigit():
        print("Invalid month"), exit()

    return month


# Data validation for year
def yearCheck():
    year = input("Enter year: ")

    if not year.isdigit():
        print("Invalid year"), exit()

    return year


def main():
    # Assign month and year from validation functions
    month = monthCheck()
    year = yearCheck()

    # println for spacing
    print()

    # Change to int's for calendar function, call month function from calendar
    month = int(month)
    year = int(year)
    print(calendar.month(year, month))


main()

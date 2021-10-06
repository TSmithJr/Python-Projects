# OwnershipCost.py


"""
MIS 15-01

this program helps the
user decide on a car
by showing the costs of
the car for 5 years
"""


# This program helps the user buy a new car


def main():
    # get user input costs

    costOfCar = eval(input("Enter the cost of the car: "))  # fixed
    milesPerYear = eval(input("How many miles will you drive each year? "))  # used w/ priceOfFuel and fuelEfficiency to calculate gas costs.
    priceOfFuel = eval(input("Enter the price of gas per gallon: "))
    fuelEfficiency = eval(input("Enter the fuel efficiency in mpg: "))
    resaleValue = eval(input("How much can you sell the car for in 5 years? "))  # deducted from total cost at end.

    # calculate the cost for one year and then 5 years

    costForOneYear = (milesPerYear / fuelEfficiency) * priceOfFuel
    costForFiveYears = costForOneYear * 5

    # calculate total cost after resale

    totalCost = (costOfCar + costForFiveYears) - resaleValue

    message = "\nThe total cost of ownership is: %.2f" % totalCost

    print(message)


# Call main
main()

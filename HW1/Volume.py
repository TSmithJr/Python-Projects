# Volume.py


"""
MIS 15-01

This program computes the volume of a bottle
with two cylinders, and a cone in between them.
It uses the volume of a cylinder formula and
the volume of a cone section formula.

Our output for volume is going to be different
because of math functions for pi. The example
volume was not completely accurate because it
used a global/normal variable for pi. The inch
value is the only value that changed, the meter
value remains the same.
"""

import math  # import math functions for the use of pi


def main():  # define main

    # assign radius 1 and 2, make them floats, acquire user input
    r1 = float(input("Enter r1(in inches): "))
    r2 = float(input("Enter r2(in inches): "))

    # assign height 1,2,3, make them floats, acquire user input
    h1 = float(input("Enter h1(in inches): "))
    h2 = float(input("Enter h2(in inches): "))
    h3 = float(input("Enter h3(in inches): "))

    print()  # print line for spacing

    # printing bottom and top radius with 2 decimal places
    print("Bottom radius: " + "%.2f" % r1 + " Inches")
    print("Top radius: " + "%.2f" % r2 + " Inches")

    # printing all 3 heights with 2 decimal places
    print("Height of bottom cylinder: " + "%.2f" % h1 + " Inches")
    print("Height of top cylinder: " + "%.2f" % h2 + " Inches")
    print("Height of cone: " + "%.2f" % h3 + " Inches")

    print()  # print line for spacing

    # formula section
    cylinderOneVolume = math.pi * r1 ** 2 * h1

    cylinderTwoVolume = math.pi * r2 ** 2 * h2

    radiusCone = (r1 ** 2 + (r1 * r2) + r2 ** 2)

    volumeCone = math.pi * ((radiusCone * h3) / 3)

    volume = cylinderOneVolume + cylinderTwoVolume + volumeCone

    # conversion from cubic inches to cubic meters, according to google
    meter_conversion = volume / 61023.744

    # printing the final output with format according to assignment sheet
    print("Volume of bottle is: " + "%.2f" % volume + " Cubic Inches or "
          + "%.4f" % meter_conversion + " Cubic Meters")


main()  # call main

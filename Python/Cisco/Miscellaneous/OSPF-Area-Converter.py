# Convert a standard integer-based area number into dotted-decimal

# Import necessary libraries
import sys
import re


def ConvertToDD():
    # Ask user for standard integer-based OSPF area number
    try:
        area_num = int(input("Please enter an integer-based OSPF area number (e.g. 1). "))
    except TypeError as e:
        print("Error:", e)
        sys.exit()

    # Check that number is valid 32-bit number
    if not (0 <= area_num < 2 ** 32):
        print("Invalid OSPF 32-bit area ID!")
        sys.exit()

    # Convert to 32-bit binary
    b_area = "{:032b}".format(area_num)
    if not len(b_area) == 32:
        print("ERROR: Area not converted to a 32-bit binary number.")
        sys.exit()

    # Convert each octet to decimal
    firstNum = [0, 8, 16, 24]
    secondNum = [8, 16, 24, 32]
    dottedDecimal = ""
    for i in range(0, 4):
        dottedDecimal += str(int(b_area[firstNum[i]:secondNum[i]], 2))
        if not i == 3:
            dottedDecimal += "."

    return dottedDecimal


def ConvertFromDD():
    # Ask user for dotted decimal input
    dottedDecimal = input("Please enter a dotted decimal OSPF area number. ")
    # Terminate execution of program if dotted decimal area number does not match format of regex
    if not re.match(r'^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){4}', (dottedDecimal + ".")):
        print("Invalid dotted decimal area number!")
        sys.exit()
    # Split dotted decimal at '.'
    decimalParts = dottedDecimal.split('.')
    binaryArea = ""
    for num in decimalParts:
        binaryArea += "{:08b}".format(int(num))
    intArea = int(binaryArea, 2)

    return intArea


if __name__ == "__main__":
    CTDD = True
    CFDD = True
    if CTDD:
        print(ConvertToDD())
    if CFDD:
        print(ConvertFromDD())
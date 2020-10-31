# Convert a standard integer-based area number into dotted-decimal

import sys

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
print(dottedDecimal)

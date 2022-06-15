#!/usr/bin/python3

# Define a list of all 8 cardinal directions
cardinalDirections = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

# Define dictionary of inputs
cardinalInputs = {}

# Ask for number of cardinals; if user inputs non-numeric character or a value of less than two,
# exit program with code 255 (unknown)
try:
    numberOfCardinals = int(input("How many cardinal directions are you providing? "))
    if numberOfCardinals < 2 or numberOfCardinals > len(cardinalDirections):
        raise ValueError
except ValueError:
    print("Invalid number of cardinals.",
          f"You must use numeric characters to represent a value of between 2 and {len(cardinalDirections)}",
          "cardinal directions.")
    exit(-1)

# Provide user instructions for inputting cardinal directions
print(f"When prompted, enter {numberOfCardinals} cardinal directions in abbreviated form (i.e., N, NE) to check",
      "whether they are adjacent to each other.")

# Fill cardinalInputs dictionary with cardinalDirection: index pairs given user input
while len(cardinalInputs) < numberOfCardinals:
    givenCardinal = input(f"Enter the abbreviation for cardinal direction #{len(cardinalInputs) + 1}: ")
    if (inputValue := givenCardinal.upper()) not in cardinalDirections:
        print(f"Invalid input/abbreviation given for cardinal direction #{len(cardinalInputs) + 1}")
        continue
    # Add cardinal direction + index to the dictionary. Immune to repeats; will not add a new item to dict if repeated.
    cardinalInputs[inputValue] = cardinalDirections.index(inputValue)

# Iterate through dictionary to create inverse sorted list of index values
sortedCardinalIndices = [index[1] for index in list(reversed(sorted(cardinalInputs.items(), key=lambda item: item[1])))]

# Create flag indicating whether provided cardinal directions are adjacent; only check for adjacent scenarios
adjacentFlag = False

# If the highest and lowest indices in the list are separated by 1 less than the number of items in the list,
# then all cardinal directions provided must be adjacent to each other.
if sortedCardinalIndices[-1] + (len(sortedCardinalIndices) - 1) == sortedCardinalIndices[0]:
    adjacentFlag = True

# If above check is False, then find out whether the list wraps around from the last item by checking for whether
# the index for the last item AND the index for the first item are part of the indices of the user input(s).
if {(len(cardinalDirections) - 1), 0}.issubset(set(sortedCardinalIndices)):
    # If the list wraps around, then the values are only adjacent if the number that is two less than the total number
    # of indices is either the second highest value or produces the second lowest value when subtracted from the
    # highest value.
    # I will leave the proof of this as an exercise to the reader. :)
    magicNumber = len(sortedCardinalIndices) - 2
    if sortedCardinalIndices[0] - magicNumber == sortedCardinalIndices[-2] or magicNumber == sortedCardinalIndices[1]:
        adjacentFlag = True

# If it is adjacent, tell the user. If it is not adjacent, tell the user.
if adjacentFlag:
    print(f"The cardinal directions provided {tuple(cardinalInputs.keys())} are adjacent.")
elif not adjacentFlag:
    print(f"The cardinal directions provided {tuple(cardinalInputs.keys())} are not adjacent.")



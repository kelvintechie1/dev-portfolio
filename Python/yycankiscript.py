# YYC Net Labs - Anki Script
# Written by: Kelvin Tran - May 30th, 2020 (Prefix 933)
# DISCLAIMER: This script is being provided as-is with no guarantee of functionality, availability, or support of any kind.

import json, sys, argparse


def userInput():
    moreCards = True

    originalFront = []
    originalBack = []
    reverseFront = []
    reverseBack = []
    reference = []
    tags = []

    while moreCards:
        if (var := input("Please enter the front value of the original card. ")) == "":
            print("Value required.")
            sys.exit()
        originalFront.append(var)

        if (var := input("Please enter the back value of the original card. ")) == "":
            print("Value required.")
            sys.exit()
        originalBack.append(var)

        if (var := input("Please enter the front value of the reversed card. ")) == "":
            print("Value required.")
            sys.exit()
        reverseFront.append(var)

        if (var := input("Please enter the back value of the reversed card. ")) == "":
            print("Value required.")
            sys.exit()
        reverseBack.append(var)

        if (var := input("Please enter your reference. ")) == "":
            print("Value required.")
            sys.exit()
        reference.append(var)

        tempTags = []
        tagsIndex = 0

        moreTags = True
        while moreTags:
            tempTags.append(input("Please enter the tags that you want to use, one per line. Hit Enter when you've input a tag. When you're done inputting tags, hit Enter once while the line is blank to finalize. "))

            if tempTags[tagsIndex] == "":
                moreTags = False
                tempTags.remove('')
            elif tempTags[tagsIndex] != "":
                tagsIndex += 1

        tags.append(tempTags)

        if (input("Type \"y\" to continue. Type nothing and press enter to stop. ")).lower() != "y":
            moreCards = False

    return [originalFront, originalBack, reverseFront, reverseBack, reference, tags]


# Load input JSON file and parse it as JSON, storing it in variable that is then returned
def loadInputFile(fileName):
    try:
        # Open note template file and parse as JSON
        template = json.load(file := open(fileName, "r"))

        # Initialize arrays to store data from JSON file
        originalFront = []
        originalBack = []
        reverseFront = []
        reverseBack = []
        reference = []
        tags = []

        for number, note in enumerate(notes := template["notes"]):
            # Append to the arrays initialized above the data from the JSON file with an index in the list matching the index of the card in the file.
            if (appendData := notes[number]["front"]) == "":
                print("Value required for front.")
                sys.exit()
            originalFront.append(appendData)

            if (appendData := notes[number]["back"]) == "":
                print("Value required for back.")
                sys.exit()
            originalBack.append(appendData)

            if (appendData := notes[number]["front_reverse"]) == "":
                print("Value required for front_reverse.")
                sys.exit()
            reverseFront.append(appendData)

            if (appendData := notes[number]["back_reverse"]) == "":
                print("Value required for back_reverse.")
                sys.exit()
            reverseBack.append(appendData)

            if (appendData := notes[number]["reference"]) == "":
                print("Value required for reference.")
                sys.exit()
            reference.append(appendData)

            tags.append(appendData := notes[number]["tags"])

        # Return an array consisting of sub-arrays from the arrays populated above.
        return [originalFront, originalBack, reverseFront, reverseBack, reference, tags]

    # Handle a decoding error exception - invalid JSON, cannot be parsed
    except json.JSONDecodeError:
        print("Invalid JSON in input file.")
    # Handle an exception if the file is not found
    except FileNotFoundError:
        print("Input file not found. Please try again with another file.")
    # Handle exception if the key is not found in the JSON file.
    except KeyError as e:
        print("The following JSON key wasn't found: ", e)
    # Handle any unexpected errors in an exception by exporting a "pretty-fied" error with the error code present.
    except:
        print("Unknown error: ", sys.exc_info()[0])

    # Exit the program if the program has to handle an exception
    sys.exit()


def loadOutputFile(file):
    try:
        stream = open(file, "r")
        outputJSON = json.load(stream)
        return outputJSON
    except json.JSONDecodeError:
        print("Invalid JSON in output file.")
    except FileNotFoundError:
        print("Output file not found. Please try again with another file.")
    except:
        print("Unknown error: ", sys.exc_info()[0])

    sys.exit()


# Find Note Model UUID in output JSON file
def FindNMUUID(json):
    try:
        uuid = json["note_models"][0]["crowdanki_uuid"]
        return uuid
    except json.JSONDecodeError:
        print("Invalid JSON in output file.")
    except KeyError as e:
        print("The following JSON key wasn't found: ", e)
    except:
        print("Unknown error: ", sys.exc_info()[0])

    sys.exit()


# Generate unique GUID for the card based on the GUID of the previous card
def GenerateUniqueGUID(json, prefix):
    index = 0
    foundPrefix = False
    highestWithPrefix = 0
    try:
        for iterations, value in enumerate(notes := json["notes"]):
            if notes[index]["guid"][0:3] == str(prefix):
                foundPrefix = True
                if (candidate := int(notes[index]["guid"])) > highestWithPrefix:
                    highestWithPrefix = candidate
            index += 1
    except KeyError as e:
        print("The following JSON key wasn't found: ", e)
        sys.exit()
    except:
        print("Unexpected error: ", sys.exc_info()[0])
        sys.exit()

    if foundPrefix == False:
        forwardGUID = str(prefix) + "0900001"
        reverseGUID = int(forwardGUID) + 1
    elif foundPrefix == True:
        lastGUID = highestWithPrefix
        try:
            forwardGUID = int(lastGUID) + 1
            reverseGUID = forwardGUID + 1
        except ValueError:
            print("Invalid value for GUID. Failure to convert to integer. ERROR: ValueError")
            sys.exit()
        except:
            print("Unexpected error: ", sys.exc_info()[0])
            sys.exit()

    return [forwardGUID, reverseGUID]


def WriteToFile(json, file, importFromFile, type, data, fields, flags, guid, nmuuid):
    print(json)

    # enumerate(fileJSON["notes"][0]) - enumerate all values needed for a single note


def main(args):
    # Replace the prefix below with your own prefix (example below)
    # prefix = 933
    prefix = 933

    # Replace the file name below with the file name of the deck JSON file as indicated in the example below:
    # deckJSON = "CCNP-ENCOR_v8.json"
    deckJSON = "CCNP-ENCOR_v8.json"

    # If there are flags, set the following variable True as indicated in the example below: (default: False)
    # SetFlags = True
    SetFlags = False

    # If there are flags, add your flags into a list. Default: 0
    CustomFlags = 0

    # If there is any data for the data field, please enter it below between the quotes.
    data = ""

    # If there is a custom type, please change the value of the variable below. Default: Note
    type = "Note"

    # If you are importing from a JSON file, mark the following field True (default: False, interactive mode) - for debug purposes ONLY, set to "debug" as string to bypass the conditional statement block.
    importFromFile = False

    if importFromFile == True:
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", help="Input JSON file")
        args = parser.parse_args()

    # Replace the file name below with the file name of the imported JSON file (example below)
    # importJSON = "note_template.json"
    # Note that if the JSON file is provided with the -f flag, it will take precedence. You do NOT need to change this if the file name is provided through -f.

    if importFromFile == True:
        if args.f != None:
            importJSON = args.f
        else:
            importJSON = "note_template.json"
        values = loadInputFile(importJSON)  # Call function to parse the value of the importJSON file as JSON
    elif importFromFile == False:
        values = userInput()  # Call userInput function to collect user input
    elif importFromFile.lower() == "debug":  # Don't collect user input or collect from file if debug is enabled.
        pass
    else:
        print("Invalid keyword for importFromFile variable. It should be a boolean True/False.")
        sys.exit()

    # Parse JSON in output file
    outputJSON = loadOutputFile(deckJSON)

    # Find the Note Model UUID to add onto all notes by calling a function to search the deck JSON file for it
    uuid = FindNMUUID(outputJSON)

    # Generate Unique GUID
    guids = GenerateUniqueGUID(outputJSON, prefix)

    # Call function to write all gathered data to deck file
    WriteToFile(outputJSON, deckJSON, importFromFile, type, data, values, CustomFlags, guids, uuid)

def ExecuteMain():
    if __name__ == "__main__":
        main(None)

ExecuteMain()

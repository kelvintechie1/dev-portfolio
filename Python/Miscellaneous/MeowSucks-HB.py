import re
import sys

def HB(RE):
    if re.match(".*", RE):
        return "Happy Birthday! Meow Sucks"
    else:
        return "Wow, he doesn't suck!"


def main():
    print(HB(String := input("Type in a command! ")))


if __name__ == "__main__":
    main()
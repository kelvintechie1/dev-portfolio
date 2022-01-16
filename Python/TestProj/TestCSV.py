import csv
with open("/Users/kelvintran/Desktop/lol.csv", "r") as csvFile:
    dReader = csv.DictReader(csvFile)
    dictionary = next(dReader)
print(dictionary)
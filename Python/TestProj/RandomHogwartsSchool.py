# Call potterapi and perform GET request

import requests
import time

print("In 5 seconds, you're going to be sorted by the Sorting Hat itself!")

time.sleep(5)

school = requests.get("https://www.potterapi.com/v1/sortingHat")  # Perform GET request to PotterAPI Sorting Hat function
response = {school: (school.text)}  # Store response in dictionary

print("The Sorting Hat has decided... " + response[school] + "!")  # Print school stored in dictionary

# Import necessary libraries
import requests
import json
import sys
import re
import time


def FileName():
    success = False
    while not success:
        # Ask user for file name
        fileName = input("What is the path to your reference file? ")

        # Open file
        try:
            jsonData = ""
            with open(fileName, 'r') as sourceFile:
                return (jsonData := json.loads(sourceFile.read()))
                success = True
        except FileNotFoundError as e:
            print("Error: ", e)
        except:
            print("Unknown error.")
            sys.exit()


def filterFunc(data):
    filterList = list(filter(lambda x: re.match(r'^T[1234]', x["postal"]) and not x["creds"]["advanced"], data))
    ham = []
    for i in filterList:
        ham.append(dict(i))
    # ham.sort(key=lambda x: x["postal"])
    return ham


def CallAPI(data):
    # These keys can be obtained from the MapQuest developer website
    # key = "provide your own key!"

    key = "provide your own key!"
    resourceURL = "http://www.mapquestapi.com/directions/v2/route"
    URLParams = {"key":key}

    session = requests.Session()
    session.headers = {'Accept': 'application/json'}

    postalCodesSearched = {}
    acceptableCallSigns = []
    acceptableTimes = []
    requestsCounter = 0  # To conform with the free tier's rate limit of 10 requests/hr.

    for i in data:
        if requestsCounter < 10:
            requestsCounter += 1
        elif requestsCounter == 10:
            break
            # remove break line and uncomment following lines to continue going after 1 hr
            # requestsCounter = 1
            # time.sleep(3600)

        if i["postal"] not in postalCodesSearched:
            bodyParams = '{"locations": [{"street": "8551 Bowness Rd NW", "city": "Calgary", "state": "AB", "postalCode": "T3B 0H8"}, {"postalCode":' + \
                         i["postal"] + '}]}'
            requestData = (request := session.get(resourceURL, params=URLParams, data=bodyParams)).json()
            if request.status_code != 200:
                print("Error in sending API request. ", request.status_code)
                sys.exit()

            postalCodesSearched[i["postal"]] = (realTime := requestData["route"]["realTime"])
        elif i["postal"] in postalCodesSearched:
            realTime = postalCodesSearched[i["postal"]]

        if (realTime / 60) < 45:
            acceptableCallSigns.append(i["callsign"])
            acceptableTimes.append(realTime / 60)

    return [acceptableCallSigns, acceptableTimes]


if __name__ == '__main__':
    ham = filterFunc(data=FileName())
    callsigns = CallAPI(ham)
    counter = 0
    while counter < len(callsigns[0]):
        print("Callsign: " + str(callsigns[0][counter]) + " / Time to club: " + str(callsigns[1][counter]) + " minutes")
        counter += 1


# Find information about Juniper platform
# Triggered by WebEx Teams text, sent to WebEx Teams chat

# Import necessary dependencies
from flask import *
import requests
from requests.auth import HTTPBasicAuth as HBA
import xml.etree.ElementTree as ET
import jnpr.junos as junos
import sys
import time
import json

app = Flask(__name__)

# Define WebEx Teams variables
WTbotToken = "fillinbottoken"
WTbaseURL = "https://webexapis.com/v1"
# ngrokURL = ""  # Fill every time you run ngrok for free plan (no custom subdomains)

# Define Juniper variables
JbaseURL = "fillinAPIURL"
Juser = "username"
Jpass = "password"
Jparams = {}

# Define parameters for WebEx Teams REST API
WTAPI = requests.Session()
WTAPI.headers = {"Accept": "application/json", "Authorization": ("Bearer " + WTbotToken)}
WebhookID = ""
responseBody = ""
roomId = "fillinroomid"

# Define HTTP parameters for Juniper REST API
JuniperAPI = requests.Session()
JuniperAPI.headers = {"Accept": "application/xml"}
JuniperAPI.auth = HBA(Juser, Jpass)


# Define shutdown script - Credit: Armin Ronacher, "Shutdown The Simple Server"

def CreateWebhook():
    ngrokURL = input("Enter the webhook URL. ")
    WTparams = {"name": "JC-WH", "targetUrl": ngrokURL, "resource": "messages", "event": "all",
                "filter": ("roomId=" + roomId)}
    WTWHresponse = WTAPI.post((WTbaseURL + "/webhooks"), data=WTparams)

    print(WTWHresponse.status_code)

    if (WHCStatus := WTWHresponse.status_code) == 200:
        print("Webhook successfully created with webhook ID " + (WTWHID := WTWHresponse.json()['id']))
    else:
        print("Other status code, please investigate further. Status code " + str(WHCStatus))
        raise RuntimeError("Webhook Creation Failed")

    return WTWHID


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=["DELETE"])
def ShutdownApp():
    if request.host != "127.0.0.1:8080":
        abort(401)
        return

    WebhookDelete = WTAPI.delete(WTbaseURL + "/webhooks/" + WebhookID)

    if (WHDStatus := WebhookDelete.status_code) == 200 or 204:
        print("Success! Webhook has been deleted.")
        webhookDeleted = True
    else:
        print("Other status received. You may have to delete the webhook with a manual API request. Status code " + str(
            WHDStatus))
        webhookDeleted = False

    print("Shutting down development server...")
    shutdown_server()

    responseData = '''{
    'message':'Server shut down'
    'status':'down'
    'webhookDeleted':''' + str(webhookDeleted) + '''}'''

    return Response(responseData, status=200, mimetype="application/json")


@app.route('/', methods=["POST"])
def WebhookReceive():
    requestData = request.json
    messageID = requestData["data"]["id"]
    personID = requestData["data"]["personId"]

    if personID == "fillinbotidhere":
        return Response('', 204)

    messageContent = (WTAPI.get(WTbaseURL + "/messages/" + messageID)).json()["text"]

    WTresponseParams = {"roomId":roomId}

    if messageContent == "Meow Sucks!":
        WTresponseParams["markdown"] = "```\nMeow Sucks!\nI agree!"
    elif messageContent == "More Cisco!":
        WTresponseParams["markdown"] = "```\nMore Cisco indeed!\nCSR-31(config)#hostname MeowSucks"
    else:
        WTresponseParams["markdown"] = "```\nUnrecognized command."

    WTAPI.post((WTbaseURL + "/messages"), data=WTresponseParams)

    responseData = '''{
    Data Received!
    }'''

    return Response(responseData, status=201, mimetype="application/json")


@app.route('/', methods=["GET"])
def GETRequestReceive():
    return '''More Juniper!
    <br>
    Welcome to the Juniper WebEx Teams Bot!
    <br>
    Created by: Kelvin Tran
    <br>
    Github: https://www.github.com/kelvintechie1'''


if __name__ == "__main__":
    port = 8080
    print("Flask Application Running on Port " + str(port) + ". Listening for WebEx webhooks.")

    WebhookID = CreateWebhook()

    # All other code must come before this
    try:
        app.run(port=port)
    except RuntimeError as e:
        print("Error: ", e)

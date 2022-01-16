from ncclient import manager
import xml.etree.ElementTree as ET


class IOSXE:
    def __init__(self, host, port, username, password, netconfObject=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.netconfObject = netconfObject


def connectNETCONF(IOSXEObj):
    m = manager.connect(host=IOSXEObj.host, port=IOSXEObj.port, username=IOSXEObj.username,
                        password=IOSXEObj.password, hostkey_verify = False,
                        device_params={"name": "csr"})

    return m


def main():
    sandboxCSR = IOSXE(host="sandbox-iosxe-recomm-1.cisco.com", port=830, username="developer",
                       password="C1sco12345")
    sandboxCSR.netconfObject = connectNETCONF(sandboxCSR)
    serverCap = (sandboxCSR.netconfObject).server_capabilities
    for cap in serverCap:
        print(cap)
    for i in range(0,5):
        print("----")
    runningConfig = ((sandboxCSR.netconfObject).get_config(source="running")).data_xml
    elementRunning = ET.fromstring(runningConfig)

    configHostname = """
    <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>csr-sandbox1</hostname>
    </native>
    </config>"""
    resp = (sandboxCSR.netconfObject).edit_config(configHostname, target="running")
    print(resp)


if __name__ == "__main__":
    main()
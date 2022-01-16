# Import all required VIRL2 client library dependencies
import virl2_client

client = virl2_client.ClientLibrary("https://cml", "kelvintr", "CMLpass0405", ssl_verify=False)

allLabs = (virl2_client.ClientLibrary.all_labs(client))

for item in allLabs:
    print(item)
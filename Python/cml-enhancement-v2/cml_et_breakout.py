import yaml


class CMLController:
    def __init__(self, telnet_start_port, url, extra_lf, lab_config_name, listen_address, password, populate_all,
                 ui_server_port, username, verify_tls, vnc_start_port):
        self.telnet_start_port = telnet_start_port
        self.url = url
        self.extra_lf = extra_lf
        self.lab_config_name = lab_config_name
        self.listen_address = listen_address
        self.password = password
        self.populate_all = populate_all
        self.ui_server_port = ui_server_port
        self.username = username
        self.verify_tls = verify_tls
        self.vnc_start_port = vnc_start_port


def checkConfig():
    print("Placeholder")


def runBreakoutInit():
    print("Placeholder")


def runBreakoutRun(lab):
    print("Placeholder")


def getBreakoutConfig(fileName="/Users/kelvintran/cml-enhancement-v2/config.yaml"):
    with open(fileName, 'r') as breakoutConfig:
        yamlData = yaml.load(breakoutConfig, Loader=yaml.FullLoader)
        controller = CMLController(telnet_start_port=yamlData["console_start_port"], url=yamlData["controller"],
                                   extra_lf=yamlData["extra_lf"], lab_config_name=yamlData["lab_config_name"],
                                   listen_address=yamlData["listen_address"], password=yamlData["password"],
                                   populate_all=yamlData["populate_all"], ui_server_port=yamlData["ui_server_port"],
                                   username=yamlData["username"], verify_tls=yamlData["verify_tls"],
                                   vnc_start_port=yamlData["vnc_start_port"])

    return controller

# Define device class
class Device:
    def __init__(self, host, address, user, pw, mgmtLoopback="Loopback0", mgmtLoopbackIP=None):
        self.host = host
        self.address = address
        self.user = user
        self.pw = pw
        self.mgmtLoopback = mgmtLoopback
        self.mgmtLoopbackIP = mgmtLoopbackIP
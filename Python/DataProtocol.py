class DataProtocol:
    def __init__(self):
        self.msgFlag = None
        self.Date = None

class DataProtocol_ID(DataProtocol):
    def __init__(self):
        super.__init__()
        self.mac = None
        self.ack = None

class DataProtocol_CODE(DataProtocol):
    def __init__(self):
        super.__init__()
        self.code = None

class DataProtocol_DATA(DataProtocol):
    def __init__(self):
        super.__init__()
        self.data = None
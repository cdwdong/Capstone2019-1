import json

class DataProtocol:
    def __init__(self):
        self.msgFlag = None
        self.date = None

    def getDict(self):
        return dict(msgFlag=self.msgFlag, date=self.date)

    def getJson(self):
        return json.dumps(self.getDict())

    def changeJsonToDic(self, j):
        return json.loads(j)

class DataProtocol_ID(DataProtocol):
    def __init__(self):
        super().__init__()
        self.mac = None
        self.ack = None

    def getDict(self):
        dic = dict(mac=self.mac, ack=self.ack)
        dic.update(super().getDict())
        return dic

class DataProtocol_CODE(DataProtocol):
    def __init__(self):
        super().__init__()
        self.code = None

    def getDict(self):
        dic = dict(code=self.code)
        dic.update(super().getDict())
        return dic

class DataProtocol_DATA(DataProtocol):
    def __init__(self):
        super().__init__()
        self.data = None

    def getDict(self):
        dic = dict(data=self.data)
        dic.update(self.getDict())
        return dic



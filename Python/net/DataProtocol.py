import json

class DataProtocol:
    def __init__(self):
        self.msgFlag = None
        self.date = None

    def getDict(self):
        return dict(msgFlag=self.msgFlag, date=self.date)

    ## 오버라이딩 되있으니 사용하셈
    ## getJson() : 객체내용을 제이슨형태로 받는놈
    # takeJson(json데이터) : 제이슨형태를 입력받아 객체에 저장
    def getJson(self):
        return json.dumps(self.getDict())

    def changeJsonToDic(self, j):
        return json.loads(j)

    def takeJson(self, j):
        dic = self.changeJsonToDic(j)
        self.msgFlag = dic["msgFlag"]
        self.date = dic["date"]

class DataProtocol_ID(DataProtocol):
    def __init__(self):
        super().__init__()
        self.mac = None
        self.ack = None

    def getDict(self):
        dic = dict(mac=self.mac, ack=self.ack)
        dic.update(super().getDict())
        return dic

    def takeJson(self, j):
        super().takeJson(j)
        dic = self.changeJsonToDic(j)
        self.mac = dic["mac"]
        self.ack = dic["ack"]

class DataProtocol_CODE(DataProtocol):
    def __init__(self):
        super().__init__()
        self.code = None

    def getDict(self):
        dic = dict(code=self.code)
        dic.update(super().getDict())
        return dic

    def takeJson(self, j):
        super().takeJson(j)
        dic = self.changeJsonToDic(j)
        self.code = dic["code"]

class DataProtocol_DATA(DataProtocol):
    def __init__(self):
        super().__init__()
        self.data = None
        self.increment = None

    def getDict(self):
        dic = dict(data=self.data, increment=self.increment)
        dic.update(super().getDict())
        return dic

    def takeJson(self, j):
        super().takeJson(j)
        dic = self.changeJsonToDic(j)
        self.data = dic["data"]
        self.increment = dic["increment"]


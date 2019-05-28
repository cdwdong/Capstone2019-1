import net.CommuHandler as CommuHandler
import asyncio
from Timing import *
from net.DataProtocol import *
import datetime


def openCode():
    with open("./script/Test-Serial-Script.py") as f:
        return f.read()

def writeSensorData(dataframe):
    if dataframe.msgFlag == Timing.SEND_DATA:
        with open("datafile.txt", "w") as datafile:
            datalist = dataframe.data.spilt(",")
            for d in datalist:
                datafile.write(f"{dataframe.date}    {d}\n")


async def eventHandle(reader, writer):

    flag = Timing.NONE
    msg = None

    while flag != Timing.ERROR:
        ## 타이밍 순서 NONE > ID > CODE > DATA
        ## 순으로 반복해서 순환
        if flag == Timing.NONE:
            while True:
                # 플래그가 SEND_ID 일때까지 무한반복
                msg = await reader.read()
                msg = msg.decode()
                dicmsg = DataProtocol().changeJsonToDic(msg)
                if dicmsg["msgFlag"] == Timing.SEND_ID:
                    flag = dicmsg["msgFlag"]
                    break

        elif flag == Timing.SEND_ID:
            if msg is None:
                print("Error: msg is None")
                flag = Timing.ERROR
                break
            proto_id = DataProtocol_ID()
            proto_id.takeJson(msg)

            flag = Timing.SEND_CODE

        elif flag == Timing.SEND_CODE:
            code = openCode()
            if code is None:
                print("Error: code is None")
                flag = Timing.ERROR
                break
            proto_code = DataProtocol_CODE()
            proto_code.code = code
            proto_code.date = datetime.datetime.now()
            proto_code.msgFlag = Timing.SEND_CODE
            writer.write(proto_code.getJson().encode())
            await writer.drain()
            flag = Timing.SEND_DATA

        elif flag == Timing.SEND_DATA:
            proto_data = DataProtocol_DATA()
            proto_data.msgFlag = Timing.SEND_DATA

            while True:
                datamsg = reader.read()
                proto_data.takeJson(datamsg.decord())

                if proto_data.msgFlag != Timing.SEND_DATA:
                    break
                writeSensorData(proto_data)


    code = openCode()
    if code == -1:
        return
    writer.write(code.encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()

server = CommuHandler.ServerHandler('172.26.2.32', 8888)
asyncio.run(server.start(eventHandle))

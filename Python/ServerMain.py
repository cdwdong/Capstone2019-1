import net.CommuHandler as CommuHandler
import asyncio
from Timing import *
from net.DataProtocol import *
import datetime
import logging
import logging.config


def openCode():
    with open("./test/code.txt", 'rt', encoding='UTF8') as f:
        return f.read()

def writeSensorData(dataframe):
    if dataframe.msgFlag == Timing.SEND_DATA.value:
        with open("datafile.txt", "w") as datafile:
            print(dataframe.data)
            datalist = dataframe.data.split(',')
            for d in datalist:
                datafile.write(f"{dataframe.date}    {d}\n")


async def eventHandle(reader, writer):

    flag = Timing.NONE.value
    msg = None

    while flag != Timing.ERROR.value:
        ## 타이밍 순서 NONE > ID > CODE > DATA
        ## 순으로 반복해서 순환
        if flag == Timing.NONE.value:
            while True:
                # 플래그가 SEND_ID 일때까지 무한반복
                msg = await reader.readline()
                msg = msg.decode()
                dicmsg = DataProtocol().changeJsonToDic(msg)
                if dicmsg["msgFlag"] == Timing.SEND_ID.value:
                    flag = dicmsg["msgFlag"]
                    break

        ##객체에 저장후 플래그 변환
        elif flag == Timing.SEND_ID.value:
            if msg is None:
                print("Error: msg is None")
                flag = Timing.ERROR.value
                break
            proto_id = DataProtocol_ID()
            proto_id.takeJson(msg)

            flag = Timing.SEND_CODE.value

        ##코드를 파일에서 읽고 객체에 담아 json으로 보내주기
        elif flag == Timing.SEND_CODE.value:
            code = openCode()
            if code is None:
                print("Error: code is None")
                flag = Timing.ERROR.value
                break

            proto_code = DataProtocol_CODE()
            proto_code.code = code
            proto_code.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            proto_code.msgFlag = Timing.SEND_CODE.value


            jsonmsg = proto_code.getJson() + '\n'
            writer.write(jsonmsg.encode())
            await writer.drain()

            flag = Timing.SEND_DATA.value

        ## 계속 반복하며 데이터객체를 읽어서 파일에 기록
        elif flag == Timing.SEND_DATA.value:
            proto_data = DataProtocol_DATA()
            proto_data.msgFlag = Timing.SEND_DATA.value

            while True:
                datamsg = await reader.readline()
                print(f"recived : {datamsg}")

                try:
                    proto_data.takeJson(datamsg.decode())
                except ValueError:
                    print("json 오류 발생")
                    flag = Timing.ERROR.value
                    break

                if proto_data.msgFlag != Timing.SEND_DATA.value:
                    break
                writeSensorData(proto_data)

#    while flag != Timing.ERROR.value


logging.config.fileConfig('conf/logging.conf')
logger = logging.getLogger()

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

server = CommuHandler.ServerHandler('127.0.0.1', 8888)
asyncio.run(server.start(eventHandle))

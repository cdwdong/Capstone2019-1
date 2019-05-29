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
            datalist = dataframe.data.split(',')
            for d in datalist:
                datafile.write(f"{dataframe.date}    {d}\n")


async def eventHandle(reader, writer):

    flag = Timing.NONE.value

    while flag != Timing.ERROR.value:
        logger.info("메인루프 시작")
        msg = await reader.readline()
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            msg = msg.decode()
            logger.info(f"Message Received : {msg}")
            dicmsg = DataProtocol().changeJsonToDic(msg)
            flag = dicmsg["msgFlag"]
            logger.info(f"Message Flag : {flag}")
        except ValueError:
            logger.error(f"ERROR! WRONG MESSAGE TYPE")
            flag = Timing.ERROR.value

        if flag == Timing.NONE.value:
            logger.warning("DATA TYPE IS Timing.NONE")

        ##객체에 저장후 플래그 변환
        elif flag == Timing.SEND_ID.value:
            logger.info("Timing.SEND_ID 루틴 시작")
            logger.info("DataProtocol_ID 객체 생성")
            proto_id = DataProtocol_ID()
            proto_id.takeJson(msg)

            ##코드를 파일에서 읽고 객체에 담아 json으로 보내주기
            code = openCode()
            if code is None:
                logger.error("code is None")
                flag = Timing.ERROR.value
                break

            logger.info("DataProtocol_CODE 객체 생성")
            proto_code = DataProtocol_CODE()
            proto_code.code = code
            proto_code.date = date
            proto_code.msgFlag = Timing.SEND_CODE.value

            jsonmsg = proto_code.getJson() + '\n'

            logger.info(f"Message Send : {jsonmsg}")
            writer.write(jsonmsg.encode())
            await writer.drain()

        ## 계속 반복하며 데이터객체를 읽어서 파일에 기록
        elif flag == Timing.SEND_DATA.value:
            logger.info("DataProtocol_DATA 객체 생성")
            proto_data = DataProtocol_DATA()
            proto_data.takeJson(msg)
            logger.info(f"데이터 기록 : {proto_data.data}")
            writeSensorData(proto_data)


logging.config.fileConfig('conf/logging.conf')
logger = logging.getLogger()

server = CommuHandler.ServerHandler('127.0.0.1', 8888)
asyncio.run(server.start(eventHandle))

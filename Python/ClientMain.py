import net.CommuHandler as CommuHandler
import net.DataProtocol as protocol
import asyncio
from datetime import datetime
from Timing import *

sensor_data_list = []
things_pointer = 0
sensing_pointer = 0

async def executeCode(code):

    code_obj = compile(code, '<string>', 'exec')
    exec(code_obj, globals())


def getMAC(interface='eth0'):
    # Return the MAC address of the specified interface
    try:
        str = open('/sys/class/net/%s/address' % interface).read()
    except:
        str = "00:00:00:00:00:00"
    return str[0:17]


async def eventHandle(reader, writer):

    flag = Timing.SEND_ID
    code_task = None
    send_id = protocol.DataProtocol_ID()
    send_code = protocol.DataProtocol_CODE()
    send_data = protocol.DataProtocol_DATA()

    while flag != Timing.ERROR:

        date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

# ############################### 원격실행 테스크 감시  ####################################################

        if code_task and code_task.done():
            pass

        if code_task and code_task.exception():
            flag.ERROR

        if code_task and code_task.cancelled():
            flag.ERROR

# ############################### 상태 전이하기  ####################################################

        if flag == Timing.SEND_ID:

            ethMAC = getMAC('eth0')

            # message = flag.SEND_ID + "," + date + "," + ethMAC
            """
            message = {"msgFlag": flag,
                       "date": date,
                       "mac": ethMAC}
            """
            send_id.msgFlag = flag
            send_id.date = date
            send_id.mac = ethMAC

            json_message = send_id.getJson()

            writer.write(json_message.encode("utf-8"))
            await writer.drain()

            return flag.SEND_CODE

        elif flag == Timing.SEND_CODE:
            # global code_task

            if code_task is None:
                receive = await reader.read()
                # executeCode(code.decode())
                dic = send_code.changeJsonToDic(receive)

                code = dic["code"]

                writer.close()
                await writer.wait_closed()

                code_task = asyncio.create_task(executeCode(code.decode()))

                return flag.SEND_DATA

            return flag.SEND_CODE

        elif flag == Timing.SEND_DATA:

            global sensor_data_list
            global things_pointer

            if sensor_data_list:
                data = "["

                for sensor in sensor_data_list:
                    data_value = sensor.split(',')

                    data = data + "{" + " \"id\": " + data_value[0] + "," + " \"data\": " + data_value[1] + "}"

                data = data + "]"

                send_data.msgFlag = flag
                send_data.date = date
                send_data.increment = sensing_pointer
                send_data.data = data

                json_message = send_data.getJson()

                writer.write(json_message.encode("utf-8"))
                await writer.drain()

            return flag.SEND_DATA

        elif flag == Timing.ERROR:
            print("원격코드에서 오류나 예외처리 발생")
            return flag.ERROR
        pass


client = CommuHandler.ClientHandler('52.78.166.156', 8888)
asyncio.run(client.start(eventHandle))

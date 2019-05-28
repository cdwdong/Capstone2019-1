import lib.CommuHandler as CommuHandler
import asyncio
from datetime import datetime
from Timing import *
import json

sensor_data_list = []
things_pointer = 0

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

    while flag != Timing.ERROR:

        date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

# ############################### 원격실행 테스크 감시  ####################################################

        if code_task.done():
            pass

        if code_task.exception():
            flag.ERROR

        if code_task.cancelled():
            flag.ERROR

# ############################### 상태 전이하기  ####################################################

        if flag == Timing.SEND_ID:

            ethMAC = getMAC('eth0')

            # message = flag.SEND_ID + "," + date + "," + ethMAC

            message = {"flag": flag.SEND_ID,
                       "date": date,
                       "MAC": ethMAC}

            json_message = json.dumps(message)

            writer.write(json_message.encode("utf-8"))
            await writer.drain()

            return flag.SEND_CODE

        elif flag == Timing.SEND_CODE:
            global code_task

            if code_task is None:
                code = await reader.read()
                # executeCode(code.decode())
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
                    data = data + "{" + " \"id\": " + sensor[0] + "," + " \"data\": " + sensor[1] + "}"

                data = data + "]"

                # message = Timing.SEND_DATA + "," + date + "," + data

                message = {"flag": flag.SEND_DATA,
                           "date": date,
                           "increment": things_pointer,
                           "data": data}

                json_message = json.dumps(message)

                writer.write(json_message.encode("utf-8"))
                await writer.drain()

            return flag.SEND_DATA

        elif flag == Timing.ETC:

            return flag.ERROR
        pass


client = CommuHandler.ClientHandler('52.78.166.156', 8888)
asyncio.run(client.start(eventHandle))

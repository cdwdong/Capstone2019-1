import net.CommuHandler as CommuHandler
import net.DataProtocol as protocol
import asyncio
from datetime import datetime
import time
from Timing import *

sensor_data_list = []
things_pointer = 0
sensing_pointer = 0
event_trigger = False

waiting_time = 3

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

    start = time.time()
    print("최초 연결시간 ", start)
    print(waiting_time, "초 대기 후 연결시작")
    current = 9999

    while current <= start + waiting_time:
        # writer.write("request connect".encode("utf-8"))

        current = time.time()

    print("Main Loop 시작")

    while flag != Timing.ERROR:

        date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

# ############################### 원격실행 테스크 감시  ####################################################

        if not code_task is None and code_task.done():
            pass

        if not code_task is None and code_task.exception():
            flag = Timing.ERROR

        if not code_task is None and code_task.cancelled():
            flag = Timing.ERROR

# ############################### 상태 전이하기  ####################################################
        # print("Client flag ", flag)
        if flag == Timing.SEND_ID:
            # print("ID 보내기");
            ethMAC = getMAC('eth0')

            send_id.msgFlag = 1 # json 인코딩 에러로 인하여 int형으로 변경
            send_id.date = date
            send_id.mac = ethMAC

            json_message = send_id.getJson()

            print("ID 보내기> ", json_message)

            writer.write(json_message.encode("utf-8"))
            await writer.drain()

            print("id 보내기 완료")

            flag = Timing.SEND_CODE

        elif flag == Timing.SEND_CODE:
            receive = await reader.read()
            receive = receive.decode()

            writer.close()
            await writer.wait_closed()

            print("Client Receive SEND_CODE Data > ", receive)
            if code_task is None and receive:
                # executeCode(code.decode())

                send_code.takeJson(receive)

                dic = send_code.getDict()

                code = dic["code"]

                print("Client Receive Code > ", code)

                writer.close()
                await writer.wait_closed()

                if code:
                    code_task = asyncio.create_task(executeCode(code.decode()))
                    flag = Timing.SEND_DATA
                else:
                    code_task = None

            else:
                flag = Timing.SEND_CODE

        elif flag == Timing.SEND_DATA:

            global sensor_data_list
            global things_pointer
            global event_trigger

            if sensor_data_list and event_trigger:

                data = sensor_data_list

                send_data.msgFlag = 3
                send_data.date = date
                send_data.increment = sensing_pointer
                send_data.data = data

                json_message = send_data.getJson()

                writer.write(json_message.encode("utf-8"))
                await writer.drain()

                sensor_data_list = ""

            flag = Timing.SEND_DATA

        elif flag == Timing.ERROR:
            print("원격코드에서 오류나 예외처리 발생")
            flag = Timing.SEND_ID

# client = CommuHandler.ClientHandler('52.78.166.156', 8888)

client = CommuHandler.ClientHandler('127.0.0.1', 8888)
asyncio.run(client.start(eventHandle))

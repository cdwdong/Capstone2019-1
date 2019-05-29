import net.CommuHandler as CommuHandler
import net.DataProtocol as protocol
import asyncio
from datetime import datetime
import time
from Timing import *
from threading import Thread

sensor_data_list = []
things_pointer = 0
sensing_pointer = 0
event_trigger = False

waiting_time = 3

remote_code = ""


def executeCode():

    global remote_code
    print("원격코드 실행")
    code_obj = compile(remote_code, '<string>', 'exec')
    exec(code_obj, globals())


def getMAC(interface='eth0'):
    # Return the MAC address of the specified interface
    try:
        str = open('/sys/class/net/%s/address' % interface).read()
    except:
        str = "00:00:00:00:00:00"
    return str[0:17]


async def eventHandle(reader, writer):

    flag = Timing.SEND_ID.value
    code_task = None
    send_id = protocol.DataProtocol_ID()
    send_code = protocol.DataProtocol_CODE()
    send_data = protocol.DataProtocol_DATA()

    start = time.time()
    print("최초 연결시간 ", start)
    print(waiting_time, "초 대기 후 연결시작")
    current = 9999
    prev_s = 0
    while current <= start + waiting_time:
        # writer.write("request connect".encode("utf-8"))

        current = time.time()

    print("Main Loop 시작")

    start = time.time()
    while flag != Timing.ERROR:
        current = time.time()
        date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

# ############################### 원격실행 테스크 감시  ####################################################

        #if not code_task is None and code_task.done():
         #   flag = Timing.SEND_DATA.value

       # if not code_task is None and code_task.exception():
        #    flag = Timing.ERROR.value

        #if not code_task is None and code_task.cancelled():
         #   flag = Timing.ERROR.value

# ############################### 상태 전이하기  ####################################################
       #print("Client flag ", flag)
        if flag == Timing.SEND_ID.value:
            # print("ID 보내기");
            ethMAC = getMAC('eth0')

            send_id.msgFlag = Timing.SEND_ID.value # json 인코딩 에러로 인하여 int형으로 변경
            send_id.date = date
            send_id.mac = ethMAC

            json_message = send_id.getJson() + "\n"

            print("ID 보내기> ", json_message)

            writer.write(json_message.encode())
            await writer.drain()

            #writer.write_eof()

            print("id 보내기 완료")

            flag = Timing.SEND_CODE.value

        elif flag == Timing.SEND_CODE.value:
            receive = await reader.readline()
            receive = receive.decode()

            #print("Client Receive SEND_CODE Data > ", receive)
            if code_task is None and receive:
                # executeCode(code.decode())
                send_code.takeJson(receive)
                dic = send_code.getDict()

                code = dic["code"]

                print("Client Receive Code > ", code)

                if code != None:
                    print("원격코드 실행 시작")
                    # code_task = asyncio.create_task(executeCode(code))

                    # code_task = Thread(target=executeCode, args=code)
                    global remote_code

                    remote_code = code

                    code_task = Thread(target=executeCode)
                    code_task.start()
                    # asyncio.run(code_task)
                    # await code_task

                    flag = Timing.SEND_DATA.value

                    print("나옴 ", flag)
                else:
                    #code_task = None
                    pass

            else:
                flag = Timing.SEND_DATA.value

        elif flag == Timing.SEND_DATA.value:

            global sensor_data_list
            global things_pointer
            global event_trigger

            sensor_data_list = "Test Data"

            if sensor_data_list and current - prev_s >= 1:

                print("Client Sensor Data Trans")
                data = sensor_data_list

                send_data.msgFlag = Timing.SEND_DATA.value
                send_data.date = date
                send_data.increment = sensing_pointer
                send_data.data = "Test Data,1"

                json_message = send_data.getJson() + "\n"

                print("Client Trans > ", json_message)

                writer.write(json_message.encode())
                await writer.drain()

                #writer.write_eof()

                #print("Client Trans > ",json_message)

                sensor_data_list = ""

                flag = Timing.SEND_DATA.value
                prev_s = time.time()

            elif sensor_data_list and current > start + 1:
                start = time.time()
                pass


        elif flag == Timing.ERROR.value:
            print("원격코드에서 오류나 예외처리 발생")
            flag = Timing.SEND_ID.value



# client = CommuHandler.ClientHandler('52.78.166.156', 8888)

client = CommuHandler.ClientHandler('127.0.0.1', 8888)
asyncio.run(client.start(eventHandle))

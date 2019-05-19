"""
2019-05-04

각종 Things들 관리하기

여기서 통신하기

작성자: 서지민

"""
import ThingsSerial
import asyncio
from CommuHandler import ClientHandler

class ThingsMangement(ThingsSerial):
    #사전
    things_list = {}
    things_pointer = 0
    tcp_flag = 0 #상태전이를 위한 변수

    # 생성자
    def __init__(self, things_pointer):
        self.things_pointer = things_pointer

    # 장치 등록 ThingsMain 객체를 추가하기
    def add_things(self, key, source):
        self.things_list.__setitem__(key, source)
        self.things_pointer = self.things_pointer + 1

    # 해당 장치 시리얼 읽기 그리고 라운드 로빈 스케줄링
    def serial_scheduling(self):
        for things in self.things_list:
            things.serial_readline()

    #타이밍 5개 함수
    #함수 끝날 때, 다음 상태로 전이하기 위하여 flag값 변경하기
    def tcp_1(self):
        pass

    def tcp_2(self):
        pass

    def tcp_3(self):
        pass

    def tcp_4(self):
        pass

    def tcp_5(self):
        pass


######################          클래스 끝          #########################################

things = ThingsMangement()


def add_things():
    pass


async def tcp_main(reader, writer):
    while True:
        #타이밍 5개 함수
        if things.tcp_flag is 1:
            things.tcp_1()

        elif things.tcp_flag is 2:
            things.tcp_2()

        elif things.tcp_flag is 3:
            things.tcp_3()

        elif things.tcp_flag is 4:
            things.tcp_4()

        elif things.tcp_flag is 5:
            things.tcp_5()


######################          이제 시작          #########################################

ip = "52.78.166.156"
port = 22
handle = ClientHandler(ip, port)
asyncio.run(handle.start(tcp_main))

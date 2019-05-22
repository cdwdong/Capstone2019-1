"""
2019-05-04
2019-05-19

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
  
######################          클래스 끝          #########################################

things = ThingsMangement()





######################          이제 시작          #########################################

ip = "52.78.166.156"
port = 22


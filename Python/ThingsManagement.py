"""
2019-05-04
2019-05-19

각종 Things들 관리하기

여기서 통신하기

작성자: 서지민

"""
import ThingsSerial as ts


class ThingsMangement(ts.ThingsSerial):
    #사전
    things_list = []
    things_pointer = 0

    # 생성자
    def __init__(self):
        pass

    # 장치 등록 ThingsMain 객체를 추가하기
    def add_things(self, source):
        self.things_list.append(source)
        self.things_pointer = self.things_pointer + 1

    # 해당 장치 시리얼 읽기 그리고 라운드 로빈 스케줄링
    def serial_scheduling(self):
        while True:
            for things in self.things_list:

                data = things.serial_readline()

                if data:
                    print("things ID: ", things.id)
                    print("things Name: ", things.name)
                    print("things Category: ", things.category)
                    print("things Upper_Category: ", things.upper_category)
                    print("things COM: ", things.port_number)
                    print("things baudrate: ", things.baudrate)
                    print("things Data: ", data)

    # 특정 장치에 대하여 값 보내기
    def serial_write(self, things_number, data):
        self.things_list[things_number].serial_readline(data)
  
######################          클래스 끝          #########################################


#테스트 예제코드
"""
dust_sensor = ts.ThingsSerial(0, "arduino dust_sensor", 2, 1, "COM4", 9600) # 실험용 Things 하나 생성

manager = ThingsMangement(); # 관리하는 객체 생성

manager.add_things(dust_sensor) # 관리하는 객체에다 Things 넣기

manager.serial_scheduling() # 데이터 수집 시작
"""

"""
2019-05-04
2019-05-19
2019-05-23

1. 라즈베리파이에 연결된 아두이노들로부터 센서값 파밍하기
2. 통신용 전역변수에 넣기

작성자: 서지민

"""
import ThingsSerial as ts
import sys
import glob
import serial
from datetime import datetime

#통신용 전역변수
sensor_data_list = []
things_pointer = 0
message_flag = 3 #추후 변경 일단 암거나함

class ThingsMangement(ts.ThingsSerial):
    # 사전
    things_pointer = 0
    things_list = []
    sensor_data_list = []

    # 생성자 장치들 파악 후 등록
    def __init__(self):
        COM_port_list = self.serial_ports()

        for com in COM_port_list:
            things = ts.ThingsSerial(self.things_pointer, com, 9600)
            self.add_things(things)

    # 장치 등록 ThingsMain 객체를 추가하기
    def add_things(self, source):
        self.things_list.append(source)
        self.things_pointer = self.things_pointer + 1

    def sensor_scheduling(self,things):
        data = things.serial_readline()

        if data:
            date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            print(date)
            print("things ID: ", things.id)
            print("Things Role: ", things.role)
            print("things COM: ", things.port_number)
            print("things baudrate: ", things.baudrate)
            print("things Data: ", data)

            ######################### 여기서 최종적으로 버퍼에다 데이터 쓰기
            message = str(message_flag) + "," + date + "," + str(things.id) + "," + "data"
            sensor_data_list.append(message)

    #상황처리테이블에 따라 팬속도 조절 동적/정적 가능
    def fan_scheduling(self,things):
        # serial_write(things_number, pwm 속도):
        pass

    # 각 장치들 라운드 로빈 스케줄링
    def serial_scheduling(self):
        while True:

            # 역활 구분하여 스케줄링
            for things in self.things_list:
                #print("this role is ",things.role)

                if things.role == "dust sensor":
                    self.sensor_scheduling(things)

                elif things.role == "fan":
                    #상황처리테이블
                    self.fan_scheduling(things)

    # 특정 장치에 대하여 값 보내기
    def serial_write(self, things_number, data):
        self.things_list[things_number].serial_readline(data)

    # 가용 COM포트번호 가져오기
    def serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result


######################          클래스 끝          #########################################

# 관리하는 객체 생성
manager = ThingsMangement()
things_pointer = manager.things_pointer #연결된 아두이노 합계

manager.serial_scheduling() #스케줄링하기










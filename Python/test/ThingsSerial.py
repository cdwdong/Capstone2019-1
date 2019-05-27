"""
2019-05-04
2019-05-23

아두이노 시리얼 읽기
아두이노가 하는 소리를 듣고 뭐하는 놈인지 파악하기

작성자: 서지민

"""
import iot.ThingsInfo as info
import serial

class ThingsSerial(info.ThingsInfo):

    #port_number = "/dev/ttyUSB0" #linux
    port_number = "COM4"  #windows
    baudrate = 9600

    #시리얼 객체
    things_serial = 0

    #Que buffer 데이터 수집하기
    Que_buffer = []

    #buffer pointer
    buffer_pointer = 0;

    role = "unknown"

    # 시리얼 객체를 생성
    def __init__(self, id, port_number, baudrate):

        super().__init__(id)

        self.port_number = port_number
        self.baudrate = baudrate

        self.things_serial = serial.Serial(port_number, baudrate)

        #누구인지 들어보기
        while self.role is "unknown":
            if self.things_serial.readable():
                res = self.things_serial.readline()

                res_str = res.decode("utf-8")

                print("Raw >" + res_str)

                data_list = res_str.split(',')

                self.role = data_list[0]

                print("This things role is " + self.role)

                #self.things_serial.write(1)

    def serial_readline(self):
        if self.things_serial.readable():
            res = self.things_serial.readline()
            res_str = res.decode("utf-8")

            data_list = res_str.split(',')
            data = data_list[1]
            #일단 string로 디코딩한다.
            #int로 변환할 필요없다. 어차피 시리얼할 때 다시 string으로 변환해야 한다.

            print("Recieve Serial Data > ", data)
            self.Que_buffer.append(data)
            self.buffer_pointer = self.buffer_pointer + 1

        return data

    def serial_writeline(self, pwm):
        pwm_str = str(pwm).encode("utf-8")
        self.things_serial.write(pwm_str)
        print("Trans Serial Data > ", pwm_str)

        #일단 string으로 변환한다.
        #utf-8로 인코딩한다.

#############################  클래스 끝    #########################################################


#테스트 예제 코드
"""
begin = ThingsSerial(0, "COM4", 9600)

while True:
    begin.serial_readline()
"""
"""
2019-05-04

아두이노 시리얼 읽기

작성자: 서지민

"""
import lib.ThingsInfo as info
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

    # 시리얼 객체를 생성
    def __init__(self, id, name, category, upper_category, port_number, baudrate):

        super().__init__(id, name, category, upper_category)

        self.port_number = port_number
        self.baudrate = baudrate

        self.things_serial = serial.Serial(port_number, baudrate)

    def serial_readline(self):
        if self.things_serial.readable():
            res = self.things_serial.readline()
            res_str = res.decode("utf-8")

            #일단 string로 디코딩한다.
            #int로 변환할 필요없다. 어차피 시리얼할 때 다시 string으로 변환해야 한다.

            print("Recieve Serial Data > ", res_str)
            self.Que_buffer.append(res_str)
            self.buffer_pointer = self.buffer_pointer + 1

        return res

    def serial_writeline(self, pwm):
        pwm_str = str(pwm).encode("utf-8")
        self.things_serial.write(pwm_str)
        print("Trans Serial Data > ", pwm_str)

        #일단 string으로 변환한다.
        #utf-8로 인코딩한다.

#############################  클래스 끝    #########################################################


#테스트 예제 코드
"""
begin = ThingsSerial(0, "arduino dust_sensor", 2, 1, "COM4", 9600)

while True:
    begin.serial_readline()
"""
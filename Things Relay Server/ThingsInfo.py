"""
2019-05-04

아두이노 등을 포함하는 각종 Things들의 정보

Things들의 최상위 클래스

이것을 상속 받고, 각 해당 기능을 구현한다.

작성자: 서지민

"""

# 센서값이 라즈베리로 오는 과정
# (Raspberry <- Bluetooth) <- (Bluetooth <- Arduino <- DustSensor)
class ThingsInfo:

    id = 0
    name = "Arduino DustSensor"
    port_number = 'COM4'
    baudrate = 9600
    category = "Arduino"
    upper_category = "Things" # null이면 이것이 바로 최상위 카테고리

    def __init__(self, id, name, category, upper_category):
        self.id = id
        self.name = name
        self.category = category
        self.upper_category = upper_category

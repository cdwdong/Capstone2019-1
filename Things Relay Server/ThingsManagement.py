"""
2019-05-04

각종 Things들 관리하기

작성자: 서지민

"""


class ThingsMangement:

    #사전
    things_list = {}
    things_pointer = 0

    # 생성자
    def __init__(self, things_pointer):
        self.things_pointer = things_pointer

    # 장치 등록 ThingsInfo 객체를 추가하기
    def add_things(self, key, source):
        self.things_list.__setitem__(key, source)
        self.things_pointer = self.things_pointer + 1


    # 해당 장치 시리얼 읽기
    # 스케줄링

import enum

class Timing(enum.Enum):
    ERROR = -1    # 아직 여기에 없는 상태 혹은 에러
    NONE = 0
    SEND_ID = 1     # ID 정보 주고 받을때 사용
    SEND_CODE = 2   # 스크립트 주고 받을때 사용
    SEND_DATA = 3   # 스택 데이터 주고 받을때 사용
    EXIT = 4        # 프로그램 빠져나오기 위한 상수


class 장면(object):

    def 입장(self):
        pass

class 엔진(object):

    map = ""

    def __init__(self, 장면_지도):
        self.map = 장면_지도

    def 플레이(self):
        print(self.map)


class 사망(장면):

    def 입장(self):
        pass

class 레이저_무기고(장면):

    def 입장(self):
        pass

class 함교(장면):

    def 입장(self):
        pass

class 구명정(장면):

    def 입장(self):
        pass

class 지도(object):

    def __init__(self, 시작_장면):
        pass

    def 다음_장면(self, 장면_이름):
        pass

    def 서막_장면(self):
        pass

게임_지도 = 지도('중앙복도')
게임_엔진 = 엔진(게임_지도)
게임_엔진.플레이()

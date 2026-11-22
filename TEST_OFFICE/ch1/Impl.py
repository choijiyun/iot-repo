from interface.RISEModuleIf import RISEModuleIf


class RISEModule(RISEModuleIf):
    """ch1 예제: 온도/습도 센서 모듈 (정수 데이터)"""

    def enterAction(self):
        print("ch1 enterAction")

    def leaveAction(self):
        print("ch1 leaveAction")

    def readData(self):
        dt = {}
        dt['temperature'] = 25
        dt['humidity'] = 60
        return dt

    def readData2(self):
        dt = {}
        dt['t_offset'] = 0.15
        dt['h_offset'] = 0.42
        return dt

    def readData3(self):
        dt = {}
        dt['s1'] = 'ch1'
        dt['s2'] = 'sensor'
        dt['s3'] = 'temp_humi'
        dt['s4'] = 'ok'
        dt['s5'] = 'hello'
        return dt

    def writeData(self, arg):
        print(arg)
        print('ch1 writeData')

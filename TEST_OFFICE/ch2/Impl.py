from interface.RISEModuleIf import RISEModuleIf


class RISEModule(RISEModuleIf):
    """ch2 예제: 조도/전력 측정 모듈 (실수 데이터)"""

    def enterAction(self):
        print("ch2 enterAction")

    def leaveAction(self):
        print("ch2 leaveAction")

    def readData(self):
        dt = {}
        dt['lux'] = 350
        dt['watt'] = 120
        return dt

    def readData2(self):
        dt = {}
        dt['voltage'] = 220.5
        dt['current'] = 0.54
        return dt

    def readData3(self):
        dt = {}
        dt['s1'] = 'ch2'
        dt['s2'] = 'meter'
        dt['s3'] = 'light_power'
        dt['s4'] = 'ok'
        return dt

    def writeData(self, arg):
        print(arg)
        print('ch2 writeData')

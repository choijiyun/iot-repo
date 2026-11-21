from interface.RISEModuleIf import RISEModuleIf


class RISEModule(RISEModuleIf):
    """ch3 예제: 릴레이/LED 제어 모듈 (상태 저장 + 쓰기)"""

    def __init__(self):
        self.state = {'relay': 0, 'led': 0}

    def enterAction(self):
        print("ch3 enterAction")

    def leaveAction(self):
        print("ch3 leaveAction")

    def readData(self):
        dt = {}
        dt['relay'] = self.state['relay']
        dt['led'] = self.state['led']
        return dt

    def readData2(self):
        dt = {}
        dt['duty'] = 0.75
        dt['freq'] = 1.5
        return dt

    def readData3(self):
        dt = {}
        dt['s1'] = 'ch3'
        dt['s2'] = 'actuator'
        dt['s3'] = 'relay_led'
        dt['s4'] = 'on' if self.state['relay'] else 'off'
        return dt

    def writeData(self, arg):
        # arg 예: {'relay': 1, 'led': 1}
        print(arg)
        if isinstance(arg, dict):
            for key in ('relay', 'led'):
                if key in arg:
                    self.state[key] = int(arg[key])
        print('ch3 writeData')

class CountIns:
    count = 0
    
    def __init__(self):
        CountIns.count += 1

    def __del__(self):
        CountIns.count -= 1

    def getInsNum(self):
        return self.count

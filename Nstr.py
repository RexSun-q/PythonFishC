class Nstr(str):

    def __sub__(self,other):
        return self.replace(other,'')

    # 移位操作
    def __lshift__(self,other):
        temp = self[:other]
        self = self[other:]
        self += temp
        return self

    def __rshift__(self,other):
        temp = self[:-other]
        self = self[-other:]
        self += temp
        return self

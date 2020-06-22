class C2F(float):

    def __new__(cls, arg=0):
        return float.__new__(cls,arg*1.8+32)



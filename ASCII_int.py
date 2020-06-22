class ASCIIint(int):
    def __new__(cls,arg=0):
        if type(arg)==str:
            count = 0
            for n in arg:
                count += ord(n)
            return count
        else:
            return super().__new__(cls,arg)



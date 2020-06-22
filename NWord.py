#根据单词的长度来进行比较大小

class Word(str):

    def __new__(cls,arg):
        if '' in arg:
            # value contains spaces
            arg = arg[:arg.index('')]
        return super().__new__(cls,arg)

    def __ge__(self,value):
        return len(self) >= len(value)

    def __gt__(self,value):
        return len(self) > len(value)

    def __le__(self,value):
        return len(self) <= len(value)

    def __lt__(self,value):
        return len(self) < len(value)

  

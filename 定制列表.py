class Clist(list):
    def __init__(self,*args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)
            
    def __len__(self):
        return len(self.count)

    def __getitem__(self,num):
        self.count[num] += 1
        return super().__getitem__(num)

    def __setitem__(self,num,value):
        self.count[num] += 1
        super().__setitem__(num,value)

    def __delitem__(self,num):
        del self.count[num]
        super().__delitem__(num)

    def counter(self,index):
        return self.count[index]

    def append(self,value):
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):
        del self.count[key]
        return super().pop(key)


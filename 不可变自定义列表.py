class UnList():
    def __init__(self,*args):
        self.value = [x for x in args]
        self.counter = {}.fromkeys(range(len(self.value)),0)

    def __len__(self):
        return len(self.value)

    def __getitem__(self,num):
        self.counter[num] += 1
        return self.value[num]
        

import time as t

class MyTimer():
    unit = ['Year','Month','Day','Hour','Minute','Second']
    note = 'Timer has not started'
    timegap = []
    begin = 0
    end = 0

    def start(self):
        print('Timer Starts...')
        self.begin = t.localtime()
        self.note = 'Note: Please stop timer'

    def stop(self):
        if not self.begin:
            print(self.note)
        else: 
            self.end = t.localtime()
            self.note = 'Total Time:'
            self._calc()
            print('Timer is end...')
        
    def _calc(self):
        for n in range(6):
            temp = self.end[n] - self.begin[n]
            if temp != 0:
                print(str(temp)+' '+MyTimer.unit[n],end='')

        # reset
        self.begin = 0
        self.end = 0

    def __str__(self):
        
            

t1 = MyTimer()
t2 = MyTimer()
t1.start()
t.sleep(45)
t1.stop()
t2.start()
t.sleep(15)
t2.stop()
print(t1 + t2)      
    
    

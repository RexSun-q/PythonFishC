class Ticket:

    def __init__(self,weekend=False,child=False):
        
        self.price = 100
        
        if weekend:
            self.ratio = 1.2
        else:
            self.ratio = 1

        if child:
            self.ratio = 0.5
        else:
            self.ratio = 1

    def account(self, num):

        return num * self.price * self.ratio



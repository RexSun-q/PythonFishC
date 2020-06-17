class Rectangle():
    width = 1
    height = 3

    def setRect(self,width,height):
        self.width =width
        self.height = height

    def getRect(self):
        print('Width='+str(self.width))
        print('Height='+str(self.height))

    def getArea(self):
        return self.width * self.height


        

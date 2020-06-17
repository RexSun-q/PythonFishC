import math as m

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    


class Line:
    def __init__(self,p1,p2):
        self.x_dist = p1.getX() - p2.getX()
        self.y_dist = p1.getY() - p2.getY()

        self.len = m.sqrt(self.x_dist**2 + self.y_dist**2)

    def getLen(self):
        return self.len


p1 = Point(2,5)
p2 = Point(5,9)

line1 = Line(p1,p2)

print(line1.getLen())

import random

class Fish:
    
    def __init__(self):
        self.x = random.randint(0,10)
        self.y = random.randint(0,10)

    def move(self):
        step_size = 1
        flag = random.randint(1,4)

        if flag == 1:
            if self.x + step_size > 10:
                self.x -= step_size
            self.x += step_size
            
        if flag == 2:
            if self.x - step_size < 0:
                self.x += step_size 
            self.x -= step_size
            
        if flag == 3:
            if self.y + step_size > 10:
                self.y -= step_size
            self.y += step_size
            
        if flag == 4:
            if self.y - step_size < 0:
                self.y += step_size
            self.y -= step_size
            
class Turtle:

    def __init__(self):
        self.hp = 100
        self.x = random.randint(0,10)
        self.y = random.randint(0,10)

    def move(self):
        self.hp -= 1
        step_size = random.randint(1,2)
        flag = random.randint(1,4)

        if flag == 1:
            if self.x + step_size > 10:
                self.x -= step_size
            self.x += step_size
            
        if flag == 2:
            if self.x - step_size < 0:
                self.x += step_size 
            self.x -= step_size
            
        if flag == 3:
            if self.y + step_size > 10:
                self.y -= step_size
            self.y += step_size
            
        if flag == 4:
            if self.y - step_size < 0:
                self.y += step_size
            self.y -= step_size

    def eat(self):
        self.hp += 20


# start simulation

turtle = Turtle()
fish = []
for i in range(10):
    newfish = Fish()
    fish.append(newfish)

print('---game start---')
count = 1

while True:
    if turtle.hp == 0:
        print('Turtle died')
        break

    if len(fish) == 0:
        print('Fishes all died')
        break
    
    print('Round '+str(count))
    print('Turtle Location before moving:'+str(turtle.x)+','+str(turtle.y))
    turtle.move()
    print('Turtle is moving to:'+str(turtle.x)+','+str(turtle.y))

    
    for one in fish:
        print('Fish Location before moving:'+str(one.x)+','+str(one.y))
        one.move()
        print('Fish is moving to:'+str(one.x)+','+str(one.y))
        if one.x == turtle.y and one.y == turtle.y:
            turtle.eat()
            fish.remove(one)
            print('This fish is gone')

    count += 1

print('---game finished---')
    

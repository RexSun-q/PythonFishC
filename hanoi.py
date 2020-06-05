def hanoi(n,x,y,z):
    if n < 1:
        return -1
    elif n == 1:
        print(x,"-->",z)
    else:
        hanoi(n-1,x,z,y) # move them except the last one from x to y
        print(x,"-->",z) # move the last one from x to z
        hanoi(n-1,y,z,x) # move units in y to z

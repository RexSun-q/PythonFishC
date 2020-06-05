def poweriter(x,y):
    if y == 0:
        return 1
    else:
        return x*poweriter(x,y-1)

testValue = input('enter a number:')
power = input('enter a power:')

print(testValue,"'s",power,'power is',poweriter(float(testValue), float(power)))


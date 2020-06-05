res = []
def digit(x):
    if x :
        res.insert(0,x % 10)
        digit(x//10)
    return res

print(digit(1985))

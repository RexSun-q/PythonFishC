def gcd(x,y):
    r = 1
    while r != 0:
        r = x % y
        x,y = y,r
    return x

print(gcd(18,9))

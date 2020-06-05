def gcd(x,y):
    if y:
        return gcd(y,(x%y))
    else:
        return x

print(gcd(9,18))
print(gcd(30,33))

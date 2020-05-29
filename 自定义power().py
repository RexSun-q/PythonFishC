def power(x,deg):
    res = 1
    if deg < 0:
        for i in range(-deg):
            res /= x
    else:
        for i in range(deg):
            res *= x
    return res

print(power(3,0))
print(power(2,2))
print(power(2,-1))

'''second way: using **'''

def power2(x,deg):
    res = x**deg
    return res

print(power2(3,0))

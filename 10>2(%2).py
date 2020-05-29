def dec2bin(x):
    cache = []
    res = ''
    while x:
        num = x % 2
        x = x // 2
        cache.append(num)
    while cache:
        res += str(cache.pop())
    return res

print(dec2bin(10),bin(10))

        

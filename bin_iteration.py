def biniter(x):
    
    res = ''
    
    if x:
        res = biniter(x//2)
        return res + str(x%2)
    else:
        return res

print(biniter(8))
print(bin(8))

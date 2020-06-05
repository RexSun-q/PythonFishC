def fnum(n):
    if n == 1 | n == 2:
        return 1
    temp = [0,1,1]
    for i in range(3,n+1):
        temp.append(temp[i-1]+temp[i-2])
    return temp[n]

        

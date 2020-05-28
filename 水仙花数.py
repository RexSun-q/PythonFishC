for n in range(100,1000):
    sum = 0
    temp = n
    while temp:
        sum = sum + (temp%10)**3
        temp = temp // 10
    if sum == n:
        print(n)
    n += 1
    
    

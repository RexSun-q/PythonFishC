def naciss():
    for n in range(100,1000):
        sum = 0
        target = n
        while n:
            part = n % 10
            n = n // 10
            sum += part**3
        if sum == target:
            print(target)
        else:
            continue
        
'another way: one line'

a = [i**3+j**3+k**3 for i in range(1, 10) for j in range(0, 10) for k in range(0, 10) if i*100+j*10+k == i**3+j**3+k**3]
print(a)

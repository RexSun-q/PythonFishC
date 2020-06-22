import math as m


def isPrimes(n):
    if n <= 1:
        return False
    for i in range(2, int(m.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def getPrimes(n):
    while True:
        if isPrimes(n):
            yield n
        n += 1

def total():
    total = 2
    for number in getPrimes(3):
        if number < 2000000:
            total += number
        else:
            print(total)
            return

if __name__ == '__main__':
    total()
        

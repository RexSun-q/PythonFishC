def fnumi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fnumi(n-1)+fnumi(n-2)

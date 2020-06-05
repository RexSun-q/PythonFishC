def age(x,basic):
    if x > 1:
        return age(x-1, basic)+2
    else:
        return basic

print(age(5,10))

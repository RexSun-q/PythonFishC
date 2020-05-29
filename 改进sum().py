def sum(x):
    sumnum = 0
    for each in x:
        if (type(each) == int) or (type(each) == float):
            sumnum += each
        else:
            continue
    return sumnum

list1 = [1,2,3,4,'shuhui',6]
print(sum(list1))

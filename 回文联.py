'Palindrome'
def pal(x):
    list1 = list(x)
    list2 = list(reversed(list1))
    if list1 == list2:
        print('palindrometic number')
    else:
        print('sorry')

pal('1234abcdcba4321')
pal('imsunzhiqi')

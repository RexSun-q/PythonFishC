def ishuiwen(string):
    if len(string) <= 1:
        return 1
    else:
        return ishuiwen(string[1:-1]) and (string[0] == string[-1])


string = input('输入一串字符:')
if ishuiwen(string):
    print(string,"是回文数")
else:
    print(string,"不是回文数")

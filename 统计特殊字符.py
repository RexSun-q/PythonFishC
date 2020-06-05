def countsc(*string):
    list1 = list(string)
    length = len(list1)
    for i in range(length):
        word = 0
        space = 0
        num = 0
        others = 0
        for each in list1[i]:
            if each.isalpha():
                word += 1
            elif each.isspace():
                space += 1
            elif each.isdigit():
                num += 1
            else:
                others += 1
        print('第',i,'字符数有英文字母:',word,'空格:',space,'数字:',num,'其他:',others,)

countsc('I love fish.com 123', 'I love you', 'you love 123')

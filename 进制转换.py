key = input('请输入一个整数【输入Q退出】：')
while key.upper() != 'Q':
    if key.isdigit():
        num = int(key)
        print('十进制 -> 十六进制：%d -> %x'%(num,num))
        print('十进制 ->  八进制：%d -> %o'%(num,num))
        print('十进制 ->  二进制：%d -> '%num,bin(num))
        key = input('请输入一个整数【输入Q退出】：')
    else:
        key = input('输入不合法，请重新输入：')
        
    

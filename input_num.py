def int_input(p = '请输入一个整数:'):
    while True:
        try:
            enter = int(input(p))
            break
        except:
            print('不是整数，输入有误')
    print('输入的整数为：'+str(enter))

int_input()
            

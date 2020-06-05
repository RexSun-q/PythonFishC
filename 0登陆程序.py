print('--新建用户--N/n')
print('--登陆账号--E/e')
print('--退出账号--Q/q')

datamanager = {}

while True:
    instr = input('--输入指令--:')
    if instr == 'N' or instr == 'n':
        create()

    elif instr == 'E' or instr == 'e':
        login()

    elif instr == 'Q' or instr == 'q':
        break

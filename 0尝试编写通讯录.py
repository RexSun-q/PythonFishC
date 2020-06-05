print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1:查询联系人资料 ---|')
print('|--- 2:插入新的联系人 ---|')
print('|--- 3:删除已有的联系人 ---|')
print('|--- 4:查看所有通讯录 ---|')
print('|--- 5:退出通讯录程序 ---|')

# contact
contact = {}

while True:
    instr = input("输入指令编号：")
    if instr.isdigit():
        instr = int(instr)
    else:
        print('输入有误，请重新输入')

    if instr == 1:
        name = input('请输入联系人姓名：')
        print(contact[name])

    if instr == 2:
        name = input('请输入新建联系人姓名：')
        number = input('请输入联系人电话号码：')
        temp = {name:int(number)}
        contact.update(temp)

    if instr == 3:
        name = input('请输入联系人姓名：')
        if name in contact:
            del(contact[name])
        else:
            print('您输入的联系人不存在。')
            
    if instr == 4:
        for key,value in contact.items():
            print(key,value)
        
    if instr == 5:
        break
        

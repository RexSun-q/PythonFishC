count = 3
password = "huihui"

while count:
    pw = input('Enter your password: ')
    if pw == password:
        print('Login Successfully')
        break
    elif '*' in pw:
        print('Password can not contain *')
        continue
    else:
        print('Your password is wrong and you can try it', count - 1 ,'times')
    count -= 1

        
        

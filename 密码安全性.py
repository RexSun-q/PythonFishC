''' check.py '''


symbols = "~!@#$%^&*()_=-/,.?<>;:[]{}\|"
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

key = 'yes'

while key == 'yes':
    inputpw = input('Enter your password: ')
    length = len(inputpw)
    while (inputpw.isspace() or length == 0):
        inputpw = input('Cannot be empty, Enter your password again: ')
        length = len(inputpw)
    if length <= 8:
        flag = 1
    elif 8 < length <= 16:
        flag = 2
    else:
        flag = 3
# symbols
    count = 0
    for unit in inputpw:
        if unit in symbols:
            count += 1
            break
    for unit in inputpw:
        if unit in chars:
            count += 1
            break
    for unit in inputpw:
        if unit in nums:
            count += 1
            break
    while 1:
        print('Accuracy is')
        if (flag == 1) or (count == 1):
            print('Low')
        elif (flag == 2) and (count == 2):
            print('Middle')
        else:
            print('High')
        break
    key = input("Do you want to try another one again? (yes/no)")
        
            

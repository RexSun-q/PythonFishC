def findstr(char,target):
    count = 0
    for i in range(len(target)):
        if (target[i] == char[0]) and (target[i+1] == char[1]):
            count += 1
    return int(count)

string1 = input('Enter sentence:')
char1 = input('Enter two characters:')

print("Characters display",findstr(char1,string1),"time(s)")

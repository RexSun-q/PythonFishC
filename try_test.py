try:
    file_1 = open('not_exist.txt')
    file_1.close()
except OSError as reason:
    print('something is wrong'+ str(reason))

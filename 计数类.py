class Count():
    
    def __init__(self,*args):
        if args:
            counter = 0
            for n in args:
                counter += 1
                print(n)
            print('Total arguments:'+str(counter))
        else:
            print('there is no input')

        
                

class Stack:

    def __init__(self,basic=[]):
        self.stack = basic

    def isEmpty(self):
        return not self.stack

    def push(self,obj):
        self.append(obj)

    def pop(self):
        if not self.stack:
            return Stack.stack.pop()

    def buttom(self):
        return self.stack[0]

    def top(self):
        num = len(self.stack)
        return self.stack[num-1]

    

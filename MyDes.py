class Notify():
    def __get__(self, instance, owner):
        print('正在读取资料')

    def __set__(self, instance, value):
        print('正在设置')

    def __delete__(self, instance):
        print('正在删除')

class MyDes():
    x = Notify()

# const 模块用于让Python支持常量操作

class Const():
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise TypeError('不能修改常量')

        if not name.isupper():
            raise TyperError('常量名必需为大写字母')

        self.__dict__[name] = value

    
import sys

'''
sys.models 是一个字典，它包含了从Python开始运行起，被导入的所有模块。键就是模块名，值就是模块对象。
'''

sys.modules[__name__] = Const()

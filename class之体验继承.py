#继承：子类默认继承父类所有的属性和方法

#1.定义一个类(父类)
class A(object):
# class A():     #在python中，所有类默认继承object类。object类是顶级类或基类；其他子类叫做派生类。
    def __init__(self):
        self.num = 2
    def print_info(self):
        print(self.num)

class B(A):
    pass

test1 = B()         #class实例化对象 不要忘记 ()     #子类也叫派生类。

test1.print_info()
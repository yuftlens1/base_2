#单继承 一个徒弟和一个师傅学习        看 'class之体验继承.py'
#多继承 一个徒弟和多个师傅学习
class A(object):
# class A():     ##在python中，所有类默认继承object类。object类是顶级类或基类；其他子类叫做派生类。
    def __init__(self):
        self.num = '招式2'
        self.num1 = '招式4'
    def print_info(self):
        print(self.num)

class C(object):
    def __init__(self):
        self.num = '招式3'
    def print_info(self):
        print(self.num)

class B(C,A):          #多继承
    def __init__(self):
        self.num = '子类自创招式5'
    def print_info(self):
        print(self.num)

test1 = B()

test1.print_info()#结论：如果一个类继承了多个父类，优先继承第一个父类的同名属性和方法。如果子类自己有和父类同名的方法或属性优先调用自己的。(自己有了就不坑老了)

print(B.__mro__)  #输出子类的继承关系。

# print(test1.num1)
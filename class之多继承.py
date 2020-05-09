#单继承 一个徒弟和一个师傅学习        看 'class之体验继承.py'
#多继承 一个徒弟和多个师傅学习
class A(object):                 # class A():     ##在python中，所有类默认继承object类。object类是顶级类或基类；其他子类叫做派生类。
    def __init__(self):
        self.num = '招式2'
        self.num1 = '招式4'
        self.num2 = '招式5'
    def print_info(self):
        print(self.num,self.num1)
    def print_info2(self):
        print(self.num2)

class C(object):
    def __init__(self):
        self.num = '招式3'
    def print_info(self):
        print(self.num)

class B(C,A):          #多继承
    def __init__(self):
        self.num = '子类自创招式5'
    def print_info(self):
        self.__init__()         ##下面添加了父类的同属性和方法的调用，再调用子类自己的(和父类一样的方法属性)就需要在自己的方法里添加自己的属性。
        print(self.num)         #这一篇肯定很容易忘记，看视频300集复习.

    def shifu_C(self):
        C.__init__(self)
        C.print_info(self)
    def shifu_A(self):
        A.__init__(self)
        A.print_info(self)
        # A.print_info2()       ##shifu A 有两个方法，子类B想继承两个方法就得写两个方法，不能放一个方法里面。但是一个方法可以调用多个属性。
    def shifu_A2(self): ###！！！在子类里面新建方法，然后在新建方法里面调用父类的属性和方法，以达到在子类的对象里可以调用父类的方法及属性
        A.__init__(self)           #调用指定的父类(A)属性
        A.print_info2(self)        #调用指定的父类(A)方法

class B_2(B):     #二重继承，类B_2继承子类B
    pass

test1 = B()

test1.print_info()#结论：如果一个类继承了多个父类，优先继承第一个父类的同名属性和方法。如果子类自己有和父类同名的方法或属性优先调用自己的。(自己有了就不坑老了)

print(B.__mro__)  #输出子类的继承关系。
test1.shifu_A()
test1.print_info()
test1.shifu_C()

test12 = B_2()    #二重继承，类B_2继承子类B，用B_2创建对象test12。下面的调用测试完全没问题 (多层继承)
print(B.__mro__)
test12.print_info()
test12.shifu_A()
test12.shifu_C()
test12.shifu_A2()

# print(test1.num1)

# import os
# os.remove('class之多层继承.py')   #多层继承整合到这里面了，所以删除了。class B_2
#super() 无参数可以自动查找父类。调用顺序遵循 __mro__ 类属性的顺序。比较适合单继承的使用。
#A为基本类，C继承A，D继承C
class A(object):
    def __init__(self):
        self.num = '招式2'
        self.num1 = '招式4'
        self.num2 = '招式15'
        self.__num2 = 111          ##定义私有属性  就是在正常属性前加 __   get_xx获取私有属性,set_xx修改私有属性。##定义私有方法 和定义私有属性一样。这篇只有私有属性的操作。
    def print_info(self):
        print(self.num,self.num1)
    def print_info2(self):
        print(self.num2)
    def get_num2(self):            #获取私有属性的方法，该方法本身不少私有的，子类可以调用到。
        return self.__num2
    def set_num2(self):            #修改私有属性的方法，想要展示修改后的效果，必须要在对象里调用一下该方法才修改。
        self.__num2 = '大威天龙'

class C(A):
    def __init__(self):
        self.num = 'C招式13'
    def print_info(self):
        print(self.num)
        super().__init__()
        super().print_info()

class D(C):
    def __init__(self):
        self.num = 'D招式3'
    def print_info(self):
        print(self.num)

    def all(self):               #super是调用父类的，貌似不能调用自己的。
        super().__init__()
        super().print_info()

tudi = D()
tudi.all()

Atudi = A()
test1 = Atudi.get_num2()        #把私有属性调出来。然后输出。
print(test1)

print(tudi.get_num2())

tudi.set_num2()
print(tudi.get_num2())
#super() 无参数可以自动查找父类。调用顺序遵循 __mro__ 类属性的顺序。比较适合单继承的使用。
#A为基本类，C继承A，D继承C
class A(object):
    def __init__(self):
        self.num = '招式2'
        self.num1 = '招式4'
        self.num2 = '招式5'
    def print_info(self):
        print(self.num,self.num1)
    def print_info2(self):
        print(self.num2)


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
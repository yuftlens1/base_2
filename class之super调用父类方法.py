class A(object):
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

#需求：子类里一次调用所有父类 A和C的方法。   在'class之多继承.py'里实现:调用一个父类方法就在子类里创建一个方法去调用,很麻烦.
    '''
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
    '''

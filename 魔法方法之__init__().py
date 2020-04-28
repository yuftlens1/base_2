# __xx__()的函数叫做魔法方法，指的是具有特殊功能的的函数

#魔法方法之:__init__() 方法的作用:初始化对象  #是直接在class里添加对象(实例)属性 的函数。
class Washer():
    def __init__(self):
        '''
        __init__代替了之前的haier.width = 400  haier.heigth = 500 在class外添加对象(实例)属性，直接在class里添加对象(实例)属性。
        '''
        self.width = 300
        self.heigth = 400

    def print_info(self):
        print(f'haier的高度是{self.heigth}')
        print(f'haier的宽度是{self.width}')

haier = Washer()        #class实例出一个对象
haier.print_info()      #调用haier对象里的print_info功能

#__init__() 也可以带参数。
class Washer1():
    def __init__(self,p1,p2):   ##定义两个形参
        self.width = p1         #把两个参数的值传入到 对象(实例)属性
        self.heigth = p2
    def print_info(self):
        print(f'haier的高度是{self.heigth}')
        print(f'haier的宽度是{self.width}')
haier1 = Washer1(30,40)       #class实例出一个对象 ,并传入参数。
haier1.print_info()      #调用haier1对象里的print_info功能

haier3 = Washer1(3,5)
haier3.print_info()


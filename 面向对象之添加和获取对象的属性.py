#添加和获取对象的属性
#属性即特征，比如：洗衣机的宽度，高度，重量。。。
#对象属性可以在类外面添加获取，也可以在类里面添加获取。

#添加对象属性   语法 ： 对象名.属性名 = 值   (属性就是变量，方法就是函数)

class Washer():
    def xyf(self):
        print('洗衣服')
        print(self)
    def hg(self):
        print('烘干')
        print(self)
    def print_info(self):
        print(f'haier的宽度是{self.width}')       #类里面获取对象属性,类外面获取对象属性看 '面向对象之self.py'
        print(f'haier的宽度是{haier.heigth}')
        #self = 调用对象

haier = Washer()

haier.width = 400     #添加对象(实例)属性
haier.heigth = 500

haier.print_info()




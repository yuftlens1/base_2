#self指的是调用该函数的对象
class Washer():
    def xyf(self):
        print('洗衣服')
        print(self)
    def hg(self):
        print('烘干')
        print(self)

haier = Washer()    #用 类Washer() 创建 对象haier

print(haier)   #结果<__main__.Washer object at 0x000001DADFD04470>

haier.xyf()    #结果如下
# 结果洗衣服
# <__main__.Washer object at 0x000001DADFD04470>

haier.hg()     #结果如下
# 烘干
# <__main__.Washer object at 0x000001DADFD04470>

#！！！打印对象和打印类里函数self得到的内存地址是一样的。 所以 self指的是调用该函数的对象 。
#哪个对象调用了这个函数，self就指代的哪个对象。   self = 调用对象


#以下代码是一个类创建多个对象   #结论：一个类可以创建多个对象，但是self内存地址连了，也就是说每个对象都是独立的。
haier2 = Washer()
haier2.xyf()    #结果如下
# 洗衣服
# <__main__.Washer object at 0x0000025C66E082E8>


#以下是类外面添加获取对象属性
#添加对象属性   语法 ： 对象名.属性名 = 值      (属性就是变量，方法就是函数)
haier.width = 400
haier.heigth = 500

print(f'haier的宽度是{haier.width}')     #类外获取对象属性

#类里面获取对象属性






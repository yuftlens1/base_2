#类和对象：用类去创建一个对象。用类实例化一个对象。 #我感觉就行docker一样，用镜像去创建一个容器。
#注意！！！：要先有类，再有对象！

#类：类是对一系列具有相同特征和行为的事物的统称，是一个抽象的概念，不是真实存在的事物。
    #-特征即是属性  --变量
    #-行为即是方法  --函数
    #也就是说类里面有 变量和函数

#对象：对象和变量 很像。

#以下是定义一个 类test1()！
class test1():               #self是 '自己;自己的' 意思。 在类里可能是 '类自己' 的意思。
    def a(self):
        print('能洗衣服')
    def b(self):
        print('能烘干衣服')

print(test1)   #结果 <class '__main__.test1'>   直接打印类没有啥有用的信息。

#以下是创建对象！
haier = test1()    #创建 haier 这个对象用 类test1()
print(haier)   #结果 <__main__.test1 object at 0x0000019E76903C18>  打印出了内存地址，能打印出内存地址说明haier这个对象已经创建成功了。

#以下是调用对象！
haier.a()      #!!! 调用   #结果 能洗衣服 ！！！
haier.b()      #上面把 类test1赋到了haier上。 调用haier就相当于调用类test1，后面跟类test1里的各个函数。




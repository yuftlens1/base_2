#类对象就是类，                   实例对象就是实例/对象  #麻求烦
# 类方法
#     特点
#       需要用装饰器@classmethod来标识其为类方法。对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数。
#     使用场景
#       当方法中需要使用类对象(如访问私有类属性等)时,定义类方法
#       类方法一般和类属性配合使用
#
# @classmethod来标识某个函数为类方法

class Dog(object):
    __tooth = 10             # __  定义私有类属性。
    @classmethod             #写调用私有类属性的类方法。
    def get_tooth(cls):      #一般以cls作为第一个参数。
        return cls.__tooth

# print(Dog.__tooth)         #报错 AttributeError: 'Dog' object has no attribute '__tooth'
print(Dog.get_tooth())

wangcai = Dog()
print(wangcai.get_tooth())
# print(wangcai.__tooth)     #报错 AttributeError: 'Dog' object has no attribute '__tooth'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 静态方法
#     特点
#         需要通过装饰器@staticmethod来进行装饰，静态方法既不需要传递类对象也不需要转递实例对象(形参没有self/cls)
#         静态方法也能够通过实例对象和类对象去访问。
#     使用场景
#         当方法中 既不需要使用实例对象(如实例对象,实例属性),也不需要使用类对象(如类属性,类方法,创建实例等)时,定义静态方法
#         取消不需要的参数传递,有利于减少不必要的内存占用和性能消耗
class Dog2(object):
    @staticmethod
    def info_print():       #没有自动补出形参self/cls
        print('这是一个狗类，用于创建狗实例。。。')
xiaobai = Dog2()
Dog2.info_print()
xiaobai.info_print()

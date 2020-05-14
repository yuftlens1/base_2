'''
面向对象三大特征：
	封装
	    将属性和方法书写到class里的操作就是封装
	    封装可以为属性和方法添加私有权
	继承
	    子类默认继承父类的所有属性和方法
	    子类可以重写父类的属性和方法
    多态
        传入不同的对象，产生不同的结果         #以上两点比较明白，这点模糊。接下来学习多态。
'''
#python的多态不是必须依赖于继承，是最好依赖于继承。
#定义:多态是一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行结果。

# 多态的创建使用
#     创建父类，定义公共方法
#     定义子类，子类重写父类方法
#     创建对象，调用不同的功能，传入不同的对象，观察执行的结果

#1    创建父类，定义公共方法      #警犬和人
class Dog(object):
    def work(self):
        pass
#2    定义子类，子类重写父类方法   #定义两类表示不同的警犬
class Armydog(Dog):                                        #多态最好依赖于继承。 #子类Armydog继承父类Dog
    def work(self):
        print('追击敌人')
class Drugdog(Dog):                                        #多态最好依赖于继承。 #子类Drugdog继承父类Dog
    def work(self):
        print('搜寻毒品')

class Person(object):
    def work_with_dog(self,dog):
        dog.work()#这里必须是work。因为下面是把两个Dog的子类(Armydog和Drugdog)作为这里的形参(dog)传入。而Armydog和Drugdog都只有work一个方法。参考'面向对象实战之搬家具.py'

#3    创建对象，调用不同的功能，传入不同的对象，观察执行的结果
ad = Armydog()
dd = Drugdog()
sir = Person()
ad.work()
sir.work_with_dog(ad)
sir.work_with_dog(dd)


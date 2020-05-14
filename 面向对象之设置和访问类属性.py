#类属性就是类对象所拥有的属性，它被该类的所有实例对象所共有。
#类属性可以使用 类 或 实例对象访问。

class Dog(object):
    tooth = 10        #这就是在设置类属性

wangcai = Dog()
xiaohei = Dog()

print(Dog.tooth)     #通过类访问类属性
print(wangcai.tooth) #通过对象访问类属性
print(xiaohei.tooth) #通过对象访问类属性

# 类属性的优点
#   1.记录的某项数据始终保持一致时，则定义类属性。
#   2.实例属性要求每个对象为其单独开辟一份内存空间来记录数据，而类属性为全类所共有，仅占用一份内存，更加节省内存。

Dog.tooth = 12      #在类修改类属性的值
print(Dog.tooth)    #结果 12
print(wangcai.tooth)    #对象


print(wangcai.tooth,'通过实例对象修改类属性之前')
wangcai.tooth = 13       #在实例对象尝试修改类属性的值
print(wangcai.tooth,'通过实例对象修改类属性')
print(Dog.tooth,'通过实例对象修改类属性')
print(xiaohei.tooth)
print(wangcai.tooth,'通过实例对象修改类属性之后')
#结论：在类修改类属性的值 该类所有的实例对象调用该类属性值是修改后的。 在实例对象尝试修改类属性的值，只针对自身修改，不会影响到类和类的其他实例对象。

#实例对象的每一个属性都会在内存单独占一份空间，如果大量定义实例对象属性就比较耗费内存。
#一般数值不会变化的属性，一般定义在类属性里，减少内存的消耗。
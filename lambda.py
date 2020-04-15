#lambda用来简化函数的，如果一个函数有一个返回值，并且只有一句代码，就可以使用lambda简化该函数代码。
def test1():
    return 100
print(test1)              #输出函数的内存地址
print(test1())

#lambda
#lambda 参数列表:表达式
test2 = lambda:100                 #这句lambda没有参数列表。只有返回值100    #无参数lambda。
print('lambda测试print(test2)的结果：',test2)               #输出lambda的内存地址
print('lambda测试print(test2())的结果：',test2())

def test3(a,b):
    return a + b
result = test3(1,3)
print(result)

test4 = lambda a,b:a + b    #lambda 参数列表:表达式   #使用lambda来实现test3函数的功能。   #位置参数lambda
print(test4(2,3))

test5 = lambda a:a          #lambda 参数列表:表达式    #一个参数的lambda
result1 = test5(11)
print(result1)

test5 = lambda a,b,c=100:a + b + c    #lambda 参数列表:表达式   #使用lambda来实现test3函数的功能。#注意 c 默认(缺省)参数lambda
print(test5(2,3))
print(test5(2,3,200))                 #传入参数的时候也可以替换掉缺省参数

test6 = lambda *args:args             #可变参数,传什么输出什么。
print(test6(2,3,45))

test7 = lambda **kwargs:kwargs        #可变参数，返回键值对dict数据。
print(test7(name='python',age=20))
print(test7(呵呵='无语'))

#lambda参数形式的写法和函数一样。






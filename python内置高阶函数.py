#python内置高阶函数之 map()
#map 映射;地图的意思。
#map(func,lst)  map函数有两个参数，一个是func函数名，另一个是lst序列。func函数是有操作的，lst是有数据的列表。
    #并将结果组成新的迭代器返回。

list1 = [1,2,3,4,5]   #map动作的对象
def test1(x):    #map的动作指导函数
    return x + 1   #动作
result = map(test1,list1)
print(result)            #结果  <map object at 0x000002001B683240>  内存地址。
print(list(result))      #结果  [2, 3, 4, 5, 6]    这才是我们想要的，map处理的list1是list数据。迭代器。


#python内置高阶函数之 reduce()
#reduce(func,lst) ，其中的func函数必须有两个参数.       ！！！作用：功能函数计算的结果和序列的下一个数据做‘累计’计算。
import functools   ##想要使用reduce，必须导入functools模块。
def test2(a,b):
     return a + b   #reduce调用的效果就是 1+2+3+4+5
    #return a * b   #reduce调用的效果就是 1*2*3*4*5
result1 = functools.reduce(test2,list1)    #functools.reduce(动作函数,序列数据) #把list1里所有的数字累加起来。
print(result1)      #结果是15

#python内置高阶函数之 filter()
#iptables的过滤(默认)表就是filter。 这里的filter()函数可以用来过滤序列里的数据。
def test3(x):
    return x % 2 == 0        ## = 运算判断需要两个。变量赋值才需要1个 = 。
result2 = filter(test3,list1)
print(result2)
print(list(result2))   #结果是[2, 4] ，在动作函数里把 除2取余为0的数字给过滤出来。

#以下是filter。 lambda表达式的写法。
print(list(filter((lambda x:x % 2 == 0),list1)))    #filter((lambda 参数列表:表达式),序列数据)
#filter(动作函数,序列数据)
#lambda 参数列表:表达式




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
#reduce(func,lst) ，其中的func函数必须有两个参数.
import functools   ##想要使用reduce，必须导入functools模块。
def test2(a,b):
    return a + b
result1 = functools.reduce(test2,list1)    #functools.reduce(动作函数,数据)
print(result1)      #结果是15。




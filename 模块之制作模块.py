# 在python中，每个python文件都可以作为一个模块，模块的名字就是文件的名字。也就是说自定义模块名必须要符合标识符命名规则。
# import my_module1
from my_module1 import *
# print(my_module1.test1(1,2))
# print(my_module1.test2(2,3))

print(test1(3,3))
print(test2(3,3))           #在my_module1模块里做了 __all__ = ['test1'] 控制，所以这不能使用test2功能。但是看下面。

import my_module1
print(my_module1.test2(3,3))#直接导入模块却还能使用，__all__ = ['test1']没控制住，貌似只能控制住 from my_module1 import * 这样导入的。
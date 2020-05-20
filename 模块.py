# 方法一
# import 模块名; 模块名,功能
# math 数学模块
import math
print(math.sqrt(9))     # math 的 sqrt 功能是计算开平方的，9的开平方是3(3的平方是9)


# 方法二
# from 模块名 import 功能1,功能2,功能3        (功能调用，省去了书写 模块名.功能)
from math import sqrt
print(sqrt(9))                             #直接用功能就行。


# 方法三
# from 模块名 import *                      #导入某个模块里的所有功能
from math import *
print(sqrt(9))
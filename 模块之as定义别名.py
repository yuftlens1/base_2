# as 定义别名

# 模块定义别名
# import 模块名 as 别名
import time as tt
tt.sleep(2)           # tt现在就是time模块
print('hello')


# 功能定义别名
# from 模块名 import 功能 as 别名
from math import sqrt as kaipingfang
print(kaipingfang(9))           # kaipingfang 现在就相当于 math.sqrt

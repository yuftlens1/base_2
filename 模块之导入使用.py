# # import 包名.模块名                       #导入包。
# import mypackage.test1,mypackage.test2
#
# # 包名.模块.功能()                          调用功能
# mypackage.test1.info_print1()
# mypackage.test2.info_print2()

from mypackage import *
test1.info_print1()
test2.info_print2()    #在包里的init文件里做了__all__ = ['test1']  以控制 from mypackage import * 这样的导入方式。


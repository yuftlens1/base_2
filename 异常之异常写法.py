#异常的写法
# tre:
#     可能发生异常的代码
# execpt:
#     如果出现异常,执行的代码
try:
    f = open('test.txt','r')
    print(f.read())
except:
    f = open('testa.txt','r')
    print(f.read())
# print(1/0)

#捕获异常代码
# tre:                                     #一般try下方只放一行尝试执行的代码。
#     可能发生异常的代码
# execpt 异常类型:                          #如果尝试执行代码的异常类型和要捕获指定的异常类型不一致，则无法捕捉异常。
#     如果捕获到该异常类型，执行的代码
# print(num)                  #报错 NameError: name 'num' is not defined   。该报错类型是NameError
"""
try:
    print(num)
except ZeroDivisionError:    #不会执行下面的代码块，因为 print(num)的报错类型是NameError，而这里指定的是 ZeroDivisionError 该类型。
    print('有错误')
"""

try:
    print(num)
except (ZeroDivisionError,NameError):     #也可以指定捕捉多个错误类型
    print('有错误')

try:
    print(num)
except (ZeroDivisionError,NameError) as errorinfo:     #把捕捉到的系统错误信息提示赋到变量里。
    print(errorinfo)

try:
    f = open('test.txt', 'r')
    print(num)
    print(1/0)
except Exception as errorinfo1:         # Exception 是所有程序异常类的父类。所以它是通用的错误类型。
    print(errorinfo1,'全量错误输出')     #一般try下方只放一行尝试执行的代码。 所以结果只会输出try下面的第一行代码错误信息。
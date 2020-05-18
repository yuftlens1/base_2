#无异常则执行完try下的无异常代码后，执行else。
try:
    print(1)
except Exception as result:
    print(result)
else:
    print('没有异常')

# finally:  表示的是无论是否异常都要执行的代码，例如关闭文件
try:
    print(num)
except Exception as result:
    print(result)
else:
    print('没有异常')
finally:
    print('哈哈')

# import os
# os.rename('异常之else.py','异常之else和finally.py')

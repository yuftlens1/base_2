#自己制作一个模块。

__all__ = ['test1']

def test1(a,b):
    # print(a + b)
    return a + b
def test2(a,b):
    return a * b

# test1(1,2)    #测试  #如果修改了模块代码就得修改测试信息，测试完了再注释掉。 这样子就很麻烦

#解决上面说的测试麻烦
if __name__ == '__main__':          # __name__ 是一个系统变量，是每个python文化名字的标识符
    print(test1(1,1))               #如果是在python文件本身里，则执行这个print语句！

print(__name__)           # __name__  在python文件本身里输出是 __main__   ，在其他python文件里调用输出是对应的文件名。

# !!! 所以  if __name__ == '__main__':   的功能就是判断是不是被调用了，还是在 python文件本身里 ！！！！！！！！！！
# 也就是 if __name__ == '__main__': 下缩进的代码块不会被其他python文件调用。

# import time
# print(time)
# time = 1
# print(time)       #变量名和模块名冲突了，变量名会覆盖掉模块名。
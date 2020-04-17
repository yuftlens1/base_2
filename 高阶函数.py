#高阶函数：把函数作为参数传入。    把一个函数作为参数传入另一个函数。
#简化代码，增加代码的灵活性。

#求数学绝对值函数 abs()函数
print(abs(-9))
print(abs(11))

#四舍五入函数 round() 函数
print(round(4))
print(round(4.4))
print(round(4.5))   #还是4
print(round(4.6))   #结果是5，也就是round函数6才进1.

def test1(a,b):     #普通写法
    """绝对值和四舍五入操作完成后 求和函数的普通写法"""
    # return round(abs(a)+abs(b))
    return round(abs(a))+round(abs(b))
print(test1(-3.3,-9.6))


def test2(a,b,c,d):
    """绝对值和四舍五入操作完成后 求和函数的高阶写法"""
    return d(a(b))+d(a(c))
    # return round(a(b))+round(a(c))
print(test2(abs,-8.6,-6.6,round))    #把abs函数作为参数传入到函数里。





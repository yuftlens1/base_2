# 自定义异常类，继承Exception            #就是自定义错误情况，把这些错用raise抛出到自定义类(str)里面输出给用户看。！！！
class ShortIonputError(Exception):
    def __init__(self,length,min_len):
        self.length = length
        self.min_len = min_len
    def __str__(self):
        return f'你输入的长度是{self.length},不能少于{self.min_len}个字符'

# print(ShortIonputError(1,3))   #raise和print很像。

def main():                                                 #自定义错误情况
    try:
        password = input('请输入密码')
        if len(password) < 4:                               #如果此处成立，则执行下面的 raise 抛出。
            raise ShortIonputError(len(password),3)         #raise 调用异常类。

    except Exception as  result:
        print(result)
    else:
        print('无异常') #try下的无异常代码后，执行else。 如果 "if len(password) < 4:" 成立，就去调用抛出异常的raise了。

main()
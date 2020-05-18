# 自定义异常类，继承Exception
class ShortIonputError(Exception):
    def __init__(self,length,min_len):
        self.length = length
        self.min_len = min_len
    def __str__(self):
        return f'你输入的长度是{self.length},不能少于{self.min_len}个字符'

print(ShortIonputError(1,3))   #raise和print很像。
#递归的特点：
#    函数内部自己调用自己
#    必须有出口

#以下是一个用户输入某个数字，实现该数字内数字累加和。
def sum_numbers(num):        #定义函数，加上形参
    if num == 1:                    #出口，当调到1的时候，直接退出并返回1 （也就是该函数最小加到1就停止。因为在调用的时候一直-1.）
        return 1
    return num + sum_numbers(num-1) #函数内部自己调用自己，重复调用直到遇到1.

result = sum_numbers(3)
print(result)





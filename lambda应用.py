#lambda的应用
test1 = lambda a,b: a if a < b else b    #返回值主体是三目运算符。
# 三目运算符的格式：  条件成立的表达式 if 条件 else 条件不成立的表达式
print(test1(3,2))

students = [
    {'name':'张三','age':20},
    {'name':'李四','age':21},
    {'name':'王五','age':29},
    {'name':'阿蛋','age':12}
]
students.sort(key= (lambda x:x['age']))
print(students)
students.sort(key= (lambda x:x['age']),reverse=True)  #reverse 相反;逆向的意思。reverse=True 相反为真就实现了倒序。
print(students)



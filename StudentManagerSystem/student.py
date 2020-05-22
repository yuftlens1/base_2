#面向对象实战之学院管理系统
#学员文件 student.py
class Student(object):
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
    def __str__(self):
        return f'{self.name},{self.age},{self.tel}'
aa = Student('aa',18,111)
print(aa)
#面向对象实战之学院管理系统
#管理系统文件 managerSystem.py
class StudentManager(object):
    def __init__(self):
        self.student_list = []           #存储数据所用的列表

    def run(self):
        self.load_student()              #加载文件里的学员信息
        while True:
         menu_num = int(input('请输入功能序号：'))
         if menu_num == 1:               #添加学员
             self.add_student()
             pass
         elif menu_num == 2:             #删除学员
             self.del_student()
             pass
         elif menu_num == 3:             #修改学员信息
             self.modify_student()
             pass
         elif menu_num == 4:             #查询学员信息
             self.search_student()
             pass
         elif menu_num == 5:             #显示所有学员信息
             self.showall_student()
             pass
         elif menu_num == 6:             #保存学员信息
             self.save_student()
             pass
         elif menu_num == 7:             #退出系统
             self.exit_os()
             break
    #系统功能函数
    @staticmethod
    def show_menu():                    #显示功能菜单；静态方法
        print('功能菜单')
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员信息')
        print('6.保存学员信息')
        print('7.退出系统')

    def add_student(self):
        print('添加学员')
    def del_student(self):
        print('删除学员')
    def modify_student(self):           #modify 修改
        print('修改')
    def search_student(self):           #search 搜索
        print('4.查询学员信息')
    def showall_student(self):
        print('5.显示所有学员信息')
    def save_student(self):
        print('6.保存学员信息')
    def exit_os(self):
        print('7.退出系统')
    def load_student(self):
        print('加载学员信息')
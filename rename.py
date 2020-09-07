import shutil
import xlrd
data=xlrd.open_workbook('C:\\rename\\A268\\name268.xls')#excle文件位置
sheet=data.sheets()[0] #读取第1个表
# rows=sheet.row_values(0) #读取第一行
# print(rows) #打印第一行
clou=sheet.col_values(0) #读取第一列
print(clou) #打印第一列
#print(rows,clou) #打印第一行第一列
#x=clou[1:] #去除第一行的dao第一个数
#print(x)

for i in (clou):
    shutil.copyfile("C:\\rename\\A268\\tz.docx",f"C:\\rename\\A268\\tz\\{i}.docx")
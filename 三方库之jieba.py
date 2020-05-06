import wordcloud  #关键库:词云
import requests
import re
import csv
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=170310173'
response = requests.get(url=url,headers=headers)
html_doc = response.content.decode('utf-8')  #保证文本内容正常
format = re.compile("<d.*?>(.*?)</d>")  #因为该网页有两层，所以先将该正则表达式编译成模式对象
DanMu = format.findall(html_doc)  #再返回列表
#逐个输出弹幕到.csv文件中
for i in DanMu:
   with open(r'C:\pytest\csv.csv',"a", newline='',encoding='utf-8-sig') as csvfile:
    writer= csv.writer(csvfile)
    danmu = []
    danmu.append(i)
    writer.writerow(danmu)

# 从外部.txt文件中读取大段文本，存入变量txt中
f = open('C:\pytest\csv.csv',encoding='utf-8')
txt = f.read()

# 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
w = wordcloud.WordCloud(width=1000, height=700, background_color='white', font_path='msyh.ttc')

# 将txt变量传入w的generate()方法，给词云输入文字
w.generate(txt)

# 将词云图片导出到当前文件夹
# w.to_file("C:\Users\YuFan\PycharmProjects\base_2\out.png")
w.to_file('C:\pytest\output.png')
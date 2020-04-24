'''
在Linux上如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成，比如dir、cp等命令。

在Python程序中执行这些目录和文件的操作可以使用python提供的os或sys模块。

- OS模块 -

os模块负责程序与操作系统的交互，提供了访问操作系统底层的接口。sys模块负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python的运行时环境。

os.getcwd() 获取    当前工作目录，即当前Python脚本工作的目录路径
os.chdir("dirname")改变当前脚本工作目录；相当于shell下cd
os.curdir 返回当前目录:('.')
os.pardir 返回当前目录的父目录字符串名:('..')
os.makedirs('dirname1/dirname2')可生成多层递归目录
os.removedirs('dirname1') 若目录为空 ，则删除，并地柜到上一级目录，如若也为空，则删除，以此类推
os.mkdir('dirname') 生成单级目录；相当于shell中mkdir dirname
os.rmdir("dirname") 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir("dirname") 列出指定目录下的所有文件和子目录，煲剧哦隐藏文件，并以列表方式打印
os.remove() 删除一个文件
os.rename("oldname","newname") 重命名文件/目录
os.stat("path/filename") 获取文件/目录信息
os.sep 输出操作系统特定的路径分隔符，win下为“\\”,linux下为“/”
os.linesep 输出当前平台使用的行终止符，win下为“\t\n”,linux下为“\n”
os.pathsep 输出用于分隔文件路径的字符串
os.name 输出置顶字符串指示当前使用平台。win->'nt';linux->'posix'
os.system("bash command") 运行shell命令，直接显示
os.environ 获取系统环境变量
os.path.abspath(path) 返回path规范化的绝对路径
os.path.split(path) 将path分隔成目录和文件名二元组返回
os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path) 返回path最后的文件名。如果path以/或、结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exist(path) 如果path存在，返回true；如果path不存在，返回False
os.path.isabs(path) 如果path是绝对路径，返回True
os.path.isfile(path) 如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path) 如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path[,path2[,...]])将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path) 返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path) 返回path所指向的文件或者目录的最后修改时间



- Shutil模块 -

复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过读写文件可以完成文件复制，只不过要多写很多代码。shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

copyfile(src, dst)：从源src复制到dst中去。当然前提是目标地址是具备可写权限（异常信息为IOException），如果当前的dst已存在的话就会被覆盖掉。
copymode(src, dst)：只是会复制其权限其他的东西是不会被复制的。
copystat(src, dst)：复制权限、最后访问时间、最后修改时间。
copy(src, dst) ：复制一个文件到一个文件或一个目录。
copy2(src, dst) ：在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西。
move(src, dst) ：移动一个文件到一个目录。如果源和目标在同一路径，操作相当于是rename操作，只是改名。
shutil.disk_usage()：获取当前目录磁盘信息，如total、used、free等信息。
copytree(olddir, newdir, True/Flase)：把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接。




- SYS模块 -


sys.argv[0]：命令行参数List，第一个元素是程序本身路径。
sys.modules.keys()：返回所有已经导入的模块列表。
sys.exc_info()：获取当前正在处理的异常类，exc_type、exc_value、exc_traceback当前处理的异常详细信息。
sys.exit(n)：退出程序，正常退出时exit(0)。
sys.hexversion：获取Python解释程序的版本值，16进制格式如：0x020403F0。
sys.version：获取Python解释程序的版本信息。
sys.maxint：最大的Int值。
sys.maxunicode：最大的Unicode值。
sys.modules：返回系统导入的模块字段，key是模块名，value是模块。
sys.path：返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值。
sys.platform：返回操作系统平台名称。
sys.stdout：标准输出。
sys.stdin：标准输入。
sys.stderr：错误输出。
sys.exc_clear()：用来清除当前线程所出现的当前的或最近的错误信息。
sys.exec_prefix：返回平台独立的python文件安装的位置。
sys.byteorder：本地字节规则的指示器，big-endian平台的值是’big’，little-endian平台的值是’little’。
sys.copyright：记录python版权相关的东西。
sys.api_version：解释器的C的API版本



- PyMysql模块 -

目前Python 3操作MySQL的驱动常用的有pymysql和mysqlclient。

使用这种数据库接口大多是就是执行连接数据库->执行query->提取数据->关闭连接这几个步骤。pymysql提供比较关键的对象，分别是Connection、Cursor、Result，使用方式上与MySQLdb或mysqlclient没什么差别。




- Request模块 -

Requests 是使用 Apache2 Licensed 许可证的 HTTP 库。用 Python 编写，真正的为人类着想。

Python 标准库中的 urllib2 模块提供了你所需要的大多数 HTTP 功能，但是它的 API 太渣了。它是为另一个时代、另一个互联网所创建的。它需要巨量的工作，甚至包括各种方法覆盖，来完成最简单的任务。

在Python的世界里，事情不应该这么麻烦。Requests 使用的是 urllib3，因此继承了它的所有特性。Requests 支持 HTTP 连接保持和连接池，支持使用 cookie 保持会话，支持文件上传，支持自动确定响应内容的编码，支持国际化的 URL 和 POST 数据自动编码。现代、国际化、人性化。
Requests模块安装：

pip install requests
也可以使用easy_install安装：

easy_install requests
Requests模块使用：

get
res = requests.get("https://github.com/timeline.json") ;
post
res = requests.post("http://httpbin.org/post");
put
res = requests.put("http://httpbin.org/put");
delete
res = requests.delete("http://httpbin.org/delete");
head
res = requests.head("http://httpbin.org/get") ;
options
res = requests.options("http://httpbin.org/get");


以上的HTTP方法，对于WEB系统一般只支持 GET 和 POST，有一些还支持 HEAD 方法。



带参数的请求实例：


import requests
requests.get('http://www.dict.baidu.com/s', params={'wd': 'python'})    #GET参数实例
requests.post('http://www.itwhy.org/wp-comments-post.php', data={'comment': '测试POST'})    #POST参数实例


POST发送JSON数据：

import requests
import json
r = requests.post('https://api.github.com/some/endpoint', data=json.dumps({'some': 'data'}))
print(r.json())


定制header：

import requests
import json
data = {'some': 'data'}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

r = requests.post('https://api.github.com/some/endpoint', data=data, headers=headers)
'''
print('ok')
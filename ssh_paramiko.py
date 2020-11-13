import paramiko,sys
def ssh_list(iplist):
    passwd = open("d:\\passwd.txt", encoding='utf-8')                            #指定ip列表文件#一个ip一行！
    while True:
        keylist = (passwd.readline().strip('\n'))
        if len(keylist) < 1:
            return
        try:
            transport = paramiko.Transport((iplist, 22))
            transport.connect(username='root', password=keylist)
            ssh = paramiko.SSHClient()
            ssh._transport = transport
        except Exception as keyerr:
            print(keyerr)
            continue
        else:
            sftp = paramiko.SFTPClient.from_transport(transport)
            # sftp.get(remotepath='/root/ceph-deploy-ceph.log',localpath='E:/ftp/ceph-deploy-ceph.log')    #下载文件
            sftp.put(localpath='E:/ftp/test.txt', remotepath='/root/test.txt')
            sftp.put(localpath='E:/ftp/ceph-deploy-ceph.log', remotepath='/root/ceph-deploy-ceph.log')
            stdin, stdout, stderr = ssh.exec_command('ip a | grep inet | grep "192.168."')                 #服务器端执行shell命令
            print(stdout.read().decode('utf-8'))
            print(stderr.read().decode('utf-8'))
            transport.close()
            passwd.close()
            return

ipfile = open("d:\\ip.txt",encoding='utf-8')                                    #指定密码文件#一组密码一行
while True:
    iprow = (ipfile.readline().strip('\n'))
    if len(iprow) < 1:
        break
    try:
        ssh_list(iprow)
    except Exception as iperr:
        print(iperr)
        continue
    else:
        continue
ipfile.close()
sys.exit()
# break：跳出所在的当前整个循环，到外层代码继续执行。
# continue：跳出本次循环，从下一个迭代继续运行循环，内层循环执行完毕，外层代码继续运行。
# return：直接返回函数，所有该函数体内的代码（包括循环体）都不会再执行。
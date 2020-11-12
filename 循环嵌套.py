# 以下是密码循环！！！
import paramiko
f = open("d:\\passwd.txt",encoding='utf-8')
p = open("d:\\ip.txt",encoding='utf-8')

while True:
    iprow = (p.readline().strip('\n'))
    print('ip层循环',iprow)
    if len(iprow) < 1:
        break
    while True:
        print('密码层内循环',iprow)
        row = f.readline()
        if len(row) < 1:
            break
        try:
            print('密码层try循环', iprow,row)
            transport = paramiko.Transport(iprow, 22)
            transport.connect(username='root', password=f'{row}')
            ssh = paramiko.SSHClient()
            ssh._transport = transport

            stdin, stdout, stderr = ssh.exec_command('ip a|grep inet')
            print(stdout.read().decode('utf-8'))
            print(stderr.read().decode('utf-8'))
            transport.close()
        except Exception as err:
            print(err)
            print('密码层execpt循环', iprow, row)
            pass
f.close()
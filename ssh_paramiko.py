import paramiko,sys
def ssh_list(iplist):
    passwd = open("d:\\passwd.txt", encoding='utf-8')                            #ָ��ip�б��ļ�#һ��ipһ�У�
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
            # sftp.get(remotepath='/root/ceph-deploy-ceph.log',localpath='E:/ftp/ceph-deploy-ceph.log')    #�����ļ�
            sftp.put(localpath='E:/ftp/test.txt', remotepath='/root/test.txt')
            sftp.put(localpath='E:/ftp/ceph-deploy-ceph.log', remotepath='/root/ceph-deploy-ceph.log')
            stdin, stdout, stderr = ssh.exec_command('ip a | grep inet | grep "192.168."')                 #��������ִ��shell����
            print(stdout.read().decode('utf-8'))
            print(stderr.read().decode('utf-8'))
            transport.close()
            passwd.close()
            return

ipfile = open("d:\\ip.txt",encoding='utf-8')                                    #ָ�������ļ�#һ������һ��
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
# break���������ڵĵ�ǰ����ѭ���������������ִ�С�
# continue����������ѭ��������һ��������������ѭ�����ڲ�ѭ��ִ����ϣ�������������С�
# return��ֱ�ӷ��غ��������иú������ڵĴ��루����ѭ���壩��������ִ�С�
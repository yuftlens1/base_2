import paramiko,sys

transport = paramiko.Transport(('192.168.127.129', 22))
transport.connect(username='root', password='1234')
ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('v1=`cat /etc/redhat-release` && if [ "$v1" = "CentOS Linux release 7.7.1909" ];then echo "匹配";else echo "不匹配"; fi && pwd && lsblk')
print(stdout.read().decode('utf-8'))
print(stderr.read().decode('utf-8'))

# sftp = paramiko.SFTPClient.from_transport(transport)
# sftp.get(remotepath='/root/ceph-deploy-ceph.log', localpath='E:/ftp/ceph-deploy-ceph.log')  #可以发送一个脚本判断是不是该升级
# sftp.put(localpath='E:/ftp/test.txt', remotepath='/root/test.txt')
# sftp.put(localpath='E:/ftp/ceph-deploy-ceph.log', remotepath='/root/ceph-deploy-ceph.log')
transport.close()
sys.exit()
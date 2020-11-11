import paramiko
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在known_hosts文件上的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname="192.168.131.129", port=22, username="root", password="1234")
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df -Th')
# 获取结果
result = stdout.read().decode()
# 获取错误提示（stdout、stderr只会输出其中一个）
err = stderr.read()
# 关闭连接
ssh.close()
print(stdin, result, err)


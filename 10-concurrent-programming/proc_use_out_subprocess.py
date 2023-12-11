"""
使用外部子进程完成任务，并控制输入输出

subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
"""
import subprocess

# 执行操作系统的 ls 命令
print("$ ls")
# run 方法返回一个 CompletedProcess 实例
# r = subprocess.run('ls', shell=True)
# print(r.returncode)  # 正常会返回 0
# call 方法等待命令执行完成或超时，然后返回状态码
r = subprocess.call('ls', shell=True)
print(r)  # 正常会返回 0

# 如果子进程需要输入内容，则需要可以调用 communicate 方法
print()
print("$ nslookup")
r = subprocess.Popen("nslookup", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# 传递字节参数
output, err = r.communicate(b"hankmo.com")
print(output.decode("utf-8"))
print('Exit code:', r.returncode)
# $ nslookup
# Server:		192.168.0.1
# Address:	192.168.0.1#53
#
# Non-authoritative answer:
# Name:	hankmo.com
# Address: 120.79.178.36
#
#
# Exit code: 0

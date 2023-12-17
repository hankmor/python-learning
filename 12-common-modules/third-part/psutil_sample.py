"""
psutil 不需要执行系统命令就可以监控系统状态的跨平台工具
"""

import psutil

# ================================================
# cpu 信息
# ================================================

cc = psutil.cpu_count()  # cpu逻辑核心
print(cc)  # 8
cc = psutil.cpu_count(logical=False)  # CPU物理核心
print(cc)  # 4

# cpu空闲时间
r = psutil.cpu_times()
print(r)  # scputimes(user=16560.25, nice=0.0, system=9226.91, idle=98102.96)

# 类似top命令的CPU使用率，每秒刷新一次，累计10次
for x in range(2):
    print(psutil.cpu_percent(interval=1, percpu=True))

# ================================================
# 内存信息
# ================================================

# 物理内存
print(psutil.virtual_memory())
# svmem(total=17179869184, available=6981169152, percent=59.4, used=9314516992, free=1271746560, active=5712760832, inactive=5665423360, wired=3601756160)
# 交换内存
print(psutil.swap_memory())
# sswap(total=1073741824, used=99352576, free=974389248, percent=9.3, sin=14111748096, sout=216743936)

# ================================================
# 磁盘信息
# ================================================

print(psutil.disk_partitions())  # 磁盘分区信息
print(psutil.disk_usage('/'))  # 磁盘使用情况
print(psutil.disk_io_counters())  # 磁盘IO

# ================================================
# 网络信息
# ================================================

print(psutil.net_io_counters())  # 获取网络读写字节／包的个数
print(psutil.net_if_addrs())  # 获取网络接口信息
print(psutil.net_if_stats())  # 获取网络接口状态
# print(psutil.net_connections()) # 获取网络连接信息，需要sudo运行: psutil.AccessDenied: (pid=12360)

# ================================================
# 进程信息
# ================================================

print(psutil.pids())  # 所有进程ID
print(psutil.pids()[-1:])
p = psutil.Process(psutil.pids()[-1:][0])  # 获取指定ID的进程
print("name:", p.name())  # 进程名称
print("exe:", p.exe())  # 进程exec路径
print("cwd:", p.cwd())  # 进程工作目录
print("cmdline:", p.cmdline())  # 进程启动的命令行
print("ppid:", p.ppid())  # 父进程ID
print("parend:", p.parent())  # 父进程
print("children:", p.children())  # 子进程列表
p.username()  # 进程用户名
print("create_time:", p.create_time())  # 进程创建时间
print("terminal:", p.terminal())  # 进程终端
print("cpu_times:", p.cpu_times())  # 进程使用的CPU时间
print("memory_info:", p.memory_info())  # 进程使用的内存
print("open_files:", p.open_files())  # 进程打开的文件
print("connections:", p.connections())  # 进程相关网络连接
print("num_threads:", p.num_threads())  # 进程的线程数量
# print("threads:", p.threads())  # 所有线程信息, 需要 sudo
print("environ:", p.environ())  # 进程环境变量
# print("terminate:", p.terminate())  # 结束进程

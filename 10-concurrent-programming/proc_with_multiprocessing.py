"""
虽然 windows 上没有 fork，但是 python 提供了 multiprocessing 模块可以模拟 fork 的效果，达到平台通用

multiprocessing模块提供了一个Process类来代表一个进程对象。
"""
import os
from multiprocessing import Process


def run_chd_proc(name):
    print("child process started and is running: %d, parent id: %d, name: %s" % (os.getpid(), os.getppid(), name))


# 必须在 main 模块中调用, 否则 RuntimeError
if __name__ == '__main__':
    print("main process: %d" % os.getpid())
    # 创建进程，target 为进程要执行的任务，args 为参数
    p = Process(target=run_chd_proc, args=('test-proc',))
    print("child process will start")
    # 启动子进程，之后会执行 target 定义的方法
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    # 主进程退出
    print("main process exit")
# main process: 12649
# child process will start
# child process started and is running: 12651, parent id: 12649, name: test-proc
# main process exit

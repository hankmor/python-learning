"""
进程间通信

Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
"""
import os
import random
import time
from multiprocessing import Queue, Process


# 通过 queue 机制在进程间交换数据

# 向队列写入数据
def write(queue):
    print("subprocess %d is writing data to queue" % os.getpid())
    for i in range(10):
        queue.put(i)
    print("write end")


def read(queue):
    print("subprocess %d is reading data from queue" % os.getpid())
    while True:
        data = queue.get()
        print("data: %d" % data)
        if data >= 9:
            break
    print("read end")


# 在 main 模块执行
if __name__ == '__main__':
    print("main process: %d" % os.getpid())
    # 创建队列
    queue = Queue()
    # 创建写入进程，负责写入数据
    pw = Process(target=write, args=(queue,))
    # 创建读取进程，负责读取数据
    pr = Process(target=read, args=(queue,))
    # 启动
    pw.start()
    pr.start()
    # 等到写入进程执行完成
    pw.join()
    print("main process end")

"""
使用进程池 Pool 管理多个进程
"""
import os
import time
from multiprocessing import Pool
import random


# 创建一个耗时方法，交给子进程执行
def long_time_task(name):
    print("subprocess is running: %d, parent id: %d, name: %s" % (os.getpid(), os.getppid(), name))
    start = time.time()
    time.sleep(random.random() * 3)  # 随机睡眠 3 秒
    end = time.time()
    print("subprocess finished after: %d seconds" % (end - start))


# 在main模块中运行 Pool 创建多个子进程
if __name__ == '__main__':
    print('main process id: %d' % os.getpid())
    # 创建进程池，最多同时运行 4 个进程，不设置默认为 cpu 的核心数
    p = Pool(processes=4)
    for i in range(5):
        # 异步执行任务, args 为 tuple, 注意只有一个元素的 tuple 写法
        p.apply_async(long_time_task, args=('sub-proc-' + str(i),))
    print("waiting for all subprocesses to finish")
    # 调用 join 前必须先关掉，这样就不能再继续添加进程了
    p.close()
    # 等待所有进程执行完成后返回
    p.join()
    print("main process end")

# 丛输出可以看到，4个子进程同时执行，剩余的另一个等他们完成后在执行，Pool 达到限制的作用

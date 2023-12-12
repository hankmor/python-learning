"""
多线程的多核心利用率
"""
import multiprocessing
import os
import threading


# ================================================
# 多个线程下 cpu 利用率测试
# ================================================

# 写一个死循环，看看 cpu 利用率
def loop():
    x = 0
    while True:
        x = x ^ 1


# cpu_cnt = multiprocessing.cpu_count()
# print("cpu count: ", cpu_cnt)
# # 按照 cpu 核心数创建多个线程
# for i in range(cpu_cnt):
#     # 创建线程
#     t = threading.Thread(target=loop)
#     t.start()

# 在我的 macOS 上，cpu 核心为 8，在 Activity Monitor 中查看，上边的程序 cpu 利用率略高于 100%
#
# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，
# 然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，
# 多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
#
# 所以，多线程编程在 python 中收到 GIL 锁的限制，并不能大大提高程序运行效率，可以转而考虑多进程程序
#
# 用 java 和 go 分别改写上边的程序，测试结果是它们都能够充分利用 cpu：
# https://github.com/hankmor/java-learning/blob/master/src/main/java/com/belonk/concurrent/CpuPerformance.java
# https://github.com/hankmor/go-learning/blob/main/02-advanced/goroutine/cpuuse/cpu_use_rate.go


# ================================================
# 如果改为多进程程序呢？看看是否能够充分利用cpu资源呢
# ================================================

# 注意必须在main模块下执行，即在主进程下开启多个子进程
if __name__ == '__main__':
    cpu_cnt = multiprocessing.cpu_count()
    print("cpu count: %d, pid: %d" % (cpu_cnt, os.getpid()))
    # 按照 cpu 核心数创建多个进程
    for i in range(cpu_cnt):
        p = multiprocessing.Process(target=loop, name="sub-proc-" + str(i))
        p.start()
        print("sub-proc is running: %d" % p.pid)
# 启动程序，查看 cpu 资源消耗情况，可以看到开启了 8 个子进程，每一个进程消耗 cpu 达到90% 以上，初开其他程序消耗的cpu，说明多进程模式下
# cpu 资源得到充分利用

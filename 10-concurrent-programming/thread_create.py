"""
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
"""
import threading


# 创建一个函数，用来在单独的线程中执行
def run(n):
    # 子线程
    print("thread %s is running" % threading.current_thread().name)
    for i in range(n):
        print("thread: %s, value: %d" % (threading.current_thread().name, i))
    # 子线程退出
    print("thread %s is exiting" % threading.current_thread().name)


# 主线程
print("thread %s is running" % threading.current_thread().name)
# 创建线程，target为线程执行的任务函数名称，注意不要写成 run() 了，name 为线程名称，不传则默认为 Thread-1，thread-2 等等
# args 为传递给 target 函数的参数
t = threading.Thread(target=run, name="sub-thread", args=(3,))
t.start()
# 等到线程 t 执行完成
t.join()
# 主线程退出
print("thread %s is exiting" % threading.current_thread().name)

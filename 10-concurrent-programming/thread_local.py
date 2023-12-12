"""
使用 thread_local 在多线程中共享数据，不用加锁

这与 java 中的 ThreadLocal 类似
"""

import threading

# 创建全局的 local 对象，可有在各个线程间共享，前提是要先给当前线程绑定属性
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 给当前线程的 local 对象绑定一个 student 属性，然后调用子方法时可以通过 local 获取该属性
    # 必须先绑定属性才能获取，否则抛出异常
    local_school.student = name
    process_student()


# 创建两个线程
t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
# Hello, Alice (in Thread-A)
# Hello, Bob (in Thread-B)

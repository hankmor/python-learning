"""
多进程分布式程序 demo

Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，
将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

demo 程序由 master 和 worker 两个进程配合完成：
1、master：负责管理队列，向队列中放入数据，并获取任务结果
2、worker：负责从队列中获取任务，执行任务并将结果写入队列

master 和 worker 可以分布在不同的机器上，通过网络连接和 Queue 交换数据。

该实例中，任务为放入一系列随机数，让 worker 计算乘方然后返回
"""
import random
from multiprocessing import Queue
from multiprocessing.managers import BaseManager

# 创建一个任务队列和一个执行完成的结果队列，这里也可以用 queue 包下的 Queue 对象
task_queue = Queue(maxsize=1024)
result_queue = Queue(maxsize=1024)


def enq(queue):
    """
    将队列中放入任务
    :return: None
    """
    print("enq data")
    for i in range(20):
        # 获取一个随机数
        i = random.randint(1, 10000)
        # 放入队列
        queue.put(i)
    print("enq data end")


def get_results(queue):
    print("try to get results")
    for i in range(20):
        # 指定超市时间 10 秒
        r = queue.get(timeout=10)
        print("got result: %s" % r)
    print("get results end")


def get_task_queue():
    return task_queue


def get_result_queue():
    return result_queue


class QueueManager(BaseManager):
    """ 队列管理器，继承自 BaseManager，用来注册队列到网络，其他 worker 进程就可以连接并从 Queue 获取任务了 """
    pass


# 必须在 main 模块下运行
if __name__ == '__main__':
    # 通过静态方法注册队列到网络中，需要给队列取一个唯一的名称，callable 指定返回注册的队列的函数
    # 注册任务队列
    QueueManager.register('task_queue', callable=get_task_queue)
    # 注册任务结果队列
    QueueManager.register('result_queue', callable=get_result_queue)

    # 创建队列管理器，指定地址、端口，authkey 的作用在于防止其他客户端恶意链接
    queue_manager = QueueManager(address=('127.0.0.1', 3000), authkey=b"123")
    # 启动管理器
    queue_manager.start()

    # 通过 manager 获取 queue，虽然也可以直接使用私有的 _task_queue，这里模拟的是分布式场景
    _task_queue = queue_manager.task_queue()
    _result_queue = queue_manager.result_queue()
    # 放入任务
    enq(_task_queue)
    # 获取结果
    get_results(_result_queue)

    # 管理管理器，网络不再可用
    queue_manager.shutdown()
    print("master exit")

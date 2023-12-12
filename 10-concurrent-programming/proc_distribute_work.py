"""
分布式多进程 demo： worker
worker 用于计算任务，这里为计算整数的平方
"""
from multiprocessing.managers import BaseManager


def power(task_queue, result_queue):
    for i in range(20):
        # 从任务队列获取数据，超时时间为 10 秒
        n = task_queue.get(timeout=10)
        print("processing task: %d" % n)
        # 计算平方
        r = n ** 2
        # 将结果写入结果队列
        result_queue.put("%d * %d = %d" % (n, n, r))
        print("process end, result: %d" % r)


class QueueManager(BaseManager):
    pass


# 必须在 main 模块下运行
if __name__ == '__main__':
    # worker 也需要注册队列名称，不需要传入 callable， 因为队列需要通过网络获取
    QueueManager.register('task_queue')
    QueueManager.register('result_queue')

    server_addr = '127.0.0.1'
    queue_manager = QueueManager(address=(server_addr, 3000), authkey=b"123")
    print('Connect to server %s...' % server_addr)
    # 连接到 master
    queue_manager.connect()
    print("server connected")
    task_queue = queue_manager.task_queue()
    result_queue = queue_manager.result_queue()

    power(task_queue, result_queue)
    print("worker exit")

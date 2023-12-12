"""
同线程的同步：加锁
"""
import threading
import time

balance = 0


def add_money():
    # 将 balance 设置为全局变量，这样多个线程可以共享它
    global balance
    for i in range(100000):
        balance = balance + 1


def minus_money():
    global balance
    for i in range(100000):
        balance = balance - 1


safe_balance = 0
# 创建一个锁, 该所在线程中共享，只有一个线程能够拿到它并执行代码
lock = threading.Lock()


def atomic_add_money():
    global safe_balance
    for i in range(100000):
        try:
            # 先加锁，这样只有拿到锁的线程能执行该方法
            # 保证了加钱操作的原子性
            lock.acquire()
            safe_balance = safe_balance + 1
        finally:
            # 别忘记释放锁
            lock.release()


def atomic_minus_money():
    global safe_balance
    for i in range(100000):
        try:
            # 加锁保证减钱操作的原子性
            lock.acquire()
            safe_balance = safe_balance - 1
        finally:
            lock.release()


def not_safe_op():
    # 创建两个线程，一个加钱，一个减钱
    at = threading.Thread(target=add_money, name="add_money_thread")
    mt = threading.Thread(target=minus_money, name="minus_money_thread")
    # 启动线程
    at.start()
    mt.start()
    # 等待线程执行结束
    at.join()
    mt.join()
    # 多执行几次，可以看到 balance 并不是期望的0，因为加钱和减钱这两个方法中并不是满足原子操作，balance = balance + 1在计算中分为先加1再赋值的两步操作，不满足原子性
    print("balance:", balance)


def safe_op():
    # 创建两个线程，一个加钱，一个减钱
    aat = threading.Thread(target=atomic_add_money, name="amotic_add_money_thread")
    amt = threading.Thread(target=atomic_minus_money, name="amotic_minus_money_thread")
    # 启动线程
    aat.start()
    amt.start()
    # 等待线程执行结束
    aat.join()
    amt.join()
    # 多执行几次，可以看到 balance 并不是期望的0，因为加钱和减钱这两个方法中并不是满足原子操作，balance = balance + 1在计算中分为先加1再赋值的两步操作，不满足原子性
    print("safe_balance:", safe_balance)


# 现在执行，可以看到 safe_balance 始终为期望的 0，而 balance 不是
not_safe_op()
safe_op()

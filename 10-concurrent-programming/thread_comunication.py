import time, threading


def async_worker(event):
    print("worker start")
    time.sleep(5)
    print("workder end")
    event.set()


def async_worker1(cond):
    print(threading.current_thread().native_id)
    with cond:
        print("worker1 start")
        time.sleep(5)
        print("worker1 end")
        cond.notify()


def worker_checker(event):
    event.wait()
    print("worker checked")


def worker1_checker(cond):
    with cond:
        cond.wait()
        print("worker1 checked")


event = threading.Event()
cond = threading.Condition()
print(threading.current_thread().native_id)
t1 = threading.Thread(target=async_worker, args=(event,))
t2 = threading.Thread(target=async_worker1, args=(cond,))
t11 = threading.Thread(target=worker_checker, args=(event,))
t21 = threading.Thread(target=worker1_checker, args=(cond,))

# 先启动等待线程
t11.start()
t21.start()

t1.start()
t2.start()

t1.join()
t2.join()
t11.join()
t21.join()

print("main thread end")

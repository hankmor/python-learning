import asyncio
import threading
import time


async def background_task():
    while True:
        print("后台任务正在运行...")
        await asyncio.sleep(2)  # 模拟异步操作


def start_event_loop():
    # 创建一个新的事件循环
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # loop.run_forever()
    loop.run_until_complete(background_task())


# 在新线程中启动事件循环
t = threading.Thread(target=start_event_loop)
t.daemon = True
t.start()

# 在新事件循环中运行后台任务
# asyncio.run_coroutine_threadsafe(background_task(), new_loop)

# 主线程的其他操作
for i in range(5):
    print(f"主线程正在运行...{i}")
    time.sleep(1)  # 模拟主线程的其他操作

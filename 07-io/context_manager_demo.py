# Python教程27：上下文管理器

from contextlib import contextmanager
import time

# 1. 类实现上下文管理器
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"打开文件：{self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            print(f"关闭文件：{self.filename}")
            self.file.close()
        return False

# 2. 使用装饰器
@contextmanager
def timer(name):
    start = time.time()
    print(f"开始计时：{name}")
    yield
    end = time.time()
    print(f"{name}执行时间：{end - start:.4f}秒")

# 使用示例
if __name__ == "__main__":
    # 使用自定义文件管理器
    with FileManager("test_ctx.txt", "w") as f:
        f.write("Hello Context Manager")
    
    # 使用计时器
    with timer("Sleep"):
        time.sleep(0.5)

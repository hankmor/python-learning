"""
练习2：文件处理器抽象类
支持txt、csv、json格式
"""

from abc import ABC, abstractmethod
import csv
import json

class FileProcessor(ABC):
    """
    文件处理器抽象基类
    - 定义文件读写接口
    """
    
    def __init__(self, filename):
        self.filename = filename
    
    @abstractmethod
    def read(self):
        """读取文件（抽象方法）"""
        pass
    
    @abstractmethod
    def write(self, data):
        """写入文件（抽象方法）"""
        pass
    
    def exists(self):
        """检查文件是否存在（具体方法）"""
        import os
        return os.path.exists(self.filename)


class TxtProcessor(FileProcessor):
    """文本文件处理器"""
    
    def read(self):
        """读取文本文件"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"文件不存在: {self.filename}"
    
    def write(self, data):
        """写入文本文件"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(str(data))
        return f"已写入文本文件: {self.filename}"


class CSVProcessor(FileProcessor):
    """CSV文件处理器"""
    
    def read(self):
        """读取CSV文件（返回列表）"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return list(reader)
        except FileNotFoundError:
            return []
    
    def write(self, data):
        """
        写入CSV文件
        data应该是字典列表
        """
        if not data:
            return "数据为空"
        
        with open(self.filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        return f"已写入CSV文件: {self.filename}"


class JSONProcessor(FileProcessor):
    """JSON文件处理器"""
    
    def read(self):
        """读取JSON文件"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None
    
    def write(self, data):
        """写入JSON文件"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return f"已写入JSON文件: {self.filename}"


# 测试
if __name__ == "__main__":
    import tempfile
    import os
    
    # 创建临时目录
    tmpdir = tempfile.mkdtemp()
    
    print("=== TXT处理器 ===")
    txt = TxtProcessor(os.path.join(tmpdir, "test.txt"))
    print(txt.write("Hello, World!\n这是测试文本。"))
    print(f"读取内容:\n{txt.read()}")
    
    print("\n=== CSV处理器 ===")
    csv_file = CSVProcessor(os.path.join(tmpdir, "test.csv"))
    data = [
        {"name": "Alice", "age": "25", "city": "北京"},
        {"name": "Bob", "age": "30", "city": "上海"},
        {"name": "Charlie", "age": "35", "city": "深圳"}
    ]
    print(csv_file.write(data))
    print(f"读取内容:")
    for row in csv_file.read():
        print(row)
    
    print("\n=== JSON处理器 ===")
    json_file = JSONProcessor(os.path.join(tmpdir, "test.json"))
    data = {
        "users": [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 30}
        ],
        "count": 2
    }
    print(json_file.write(data))
    print(f"读取内容:")
    print(json.dumps(json_file.read(), ensure_ascii=False, indent=2))
    
    # 清理
    import shutil
    shutil.rmtree(tmpdir)
    print(f"\n临时文件已清理")

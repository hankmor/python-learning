"""
存储模块
- 负责任务数据的持久化
- 应用：文件操作、JSON、异常处理
"""

import json
import os
from pathlib import Path
from typing import List
from .task import Task  # Changed from 'from task import Task'

class TaskStorage:
    """
    任务存储类
    - 使用JSON格式存储
    - 包含完整的异常处理
    """
    
    def __init__(self, file_path="tasks.json"):
        """
        初始化存储
        
        Args:
            file_path: 存储文件路径
        """
        self.file_path = Path(file_path)
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """确保存储文件存在"""
        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")
    
    def save_tasks(self, tasks: List[Task]):
        """
        保存任务列表
        
        Args:
            tasks: 任务列表
        
        Raises:
            IOError: 文件写入失败时
        """
        try:
            data = [task.to_dict() for task in tasks]
            
            # 使用with确保文件正确关闭
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        
        except Exception as e:
            raise IOError(f"保存任务失败：{e}")
    
    def load_tasks(self) -> List[Task]:
        """
        加载任务列表
        
        Returns:
            List[Task]: 任务列表
        
        Raises:
            IOError: 文件读取失败时
        """
        try:
            with open(self.file_path, encoding="utf-8") as f:
                data = json.load(f)
            
            return [Task.from_dict(item) for item in data]
        
        except json.JSONDecodeError as e:
            raise IOError(f"JSON解析失败：{e}")
        except Exception as e:
            raise IOError(f"加载任务失败：{e}")
    
    def backup(self, backup_path=None):
        """
        备份任务数据
        
        Args:
            backup_path: 备份文件路径
        """
        if backup_path is None:
            backup_path = f"{self.file_path}.backup"
        
        import shutil
        shutil.copy(self.file_path, backup_path)

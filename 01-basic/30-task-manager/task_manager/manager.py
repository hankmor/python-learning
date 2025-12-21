"""
任务管理器
- 核心业务逻辑
- 应用：类、方法、列表操作
"""

from typing import List, Optional
from .task import Task, Priority, Category # Adjusted import
from .storage import TaskStorage # Adjusted import

class TaskManager:
    """
    任务管理器
    - 管理任务的CRUD操作
    - 提供搜索、统计等功能
    """
    
    def __init__(self, storage: TaskStorage):
        """
        初始化管理器
        
        Args:
            storage: 存储对象
        """
        self.storage = storage
        self.tasks: List[Task] = []
        self.load()
    
    def load(self):
        """加载任务"""
        try:
            self.tasks = self.storage.load_tasks()
        except IOError as e:
            print(f"警告：{e}")
            self.tasks = []
    
    def save(self):
        """保存任务"""
        try:
            self.storage.save_tasks(self.tasks)
        except IOError as e:
            print(f"错误：{e}")
    
    def add_task(self, task: Task):
        """添加任务"""
        self.tasks.append(task)
        self.save()
    
    def get_all_tasks(self) -> List[Task]:
        """获取所有任务"""
        return self.tasks
    
    def get_task(self, index: int) -> Optional[Task]:
        """
        获取指定任务
        
        Args:
            index: 任务索引
        
        Returns:
            Task或None
        """
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None
    
    def complete_task(self, index: int) -> bool:
        """标记任务完成"""
        task = self.get_task(index)
        if task:
            task.mark_complete()
            self.save()
            return True
        return False
    
    def delete_task(self, index: int) -> bool:
        """删除任务"""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save()
            return True
        return False
    
    def search_tasks(self, keyword: str) -> List[Task]:
        """
        搜索任务
        
        Args:
            keyword: 关键词
        
        Returns:
            匹配的任务列表
        """
        keyword = keyword.lower()
        return [
            task for task in self.tasks
            if keyword in task.title.lower() 
            or keyword in task.description.lower()
        ]
    
    def get_statistics(self) -> dict:
        """
        获取统计信息
        
        Returns:
            统计字典
        """
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.completed)
        pending = total - completed
        
        by_priority = {
            Priority.HIGH: 0,
            Priority.MEDIUM: 0,
            Priority.LOW: 0
        }
        
        for task in self.tasks:
            if not task.completed:
                by_priority[task.priority] += 1
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "high_priority": by_priority[Priority.HIGH],
            "medium_priority": by_priority[Priority.MEDIUM],
            "low_priority": by_priority[Priority.LOW]
        }

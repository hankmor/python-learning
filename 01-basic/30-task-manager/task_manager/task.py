"""
任务类模块
- 定义Task类表示单个任务
- 应用：类、属性、方法
"""

from datetime import datetime
from enum import Enum

class Priority(Enum):
    """
    任务优先级枚举
    - 使用Enum定义常量
    - 避免魔法数字
    """
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Category(Enum):
    """任务分类"""
    WORK = "工作"
    LIFE = "生活"
    STUDY = "学习"
    OTHER = "其他"

class Task:
    """
    任务类
    
    Attributes:
        title: 任务标题
        description: 任务描述
        priority: 优先级
        category: 分类
        due_date: 截止日期
        completed: 是否完成
        created_at: 创建时间
    """
    
    def __init__(self, title, description="", 
                 priority=Priority.MEDIUM,
                 category=Category.OTHER,
                 due_date=None):
        """
        初始化任务
        
        Args:
            title: 任务标题（必需）
            description: 任务描述
            priority: 优先级（默认中等）
            category: 分类（默认其他）
            due_date: 截止日期（datetime对象）
        
        Raises:
            ValueError: 标题为空时
        """
        if not title:
            raise ValueError("任务标题不能为空")
        
        self.title = title
        self.description = description
        self.priority = priority
        self.category = category
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.now()
    
    def mark_complete(self):
        """标记任务完成"""
        self.completed = True
    
    def mark_incomplete(self):
        """标记任务未完成"""
        self.completed = False
    
    def to_dict(self):
        """
        转换为字典（用于JSON序列化）
        
        Returns:
            dict: 任务的字典表示
        """
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority.value,
            "category": self.category.value,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        从字典创建任务（用于JSON反序列化）
        
        Args:
            data: 任务字典
        
        Returns:
            Task: 任务对象
        """
        task = cls(
            title=data["title"],
            description=data.get("description", ""),
            priority=Priority(data.get("priority", 2)),
            category=Category(data.get("category", "其他"))
        )
        
        if data.get("due_date"):
            task.due_date = datetime.fromisoformat(data["due_date"])
        
        task.completed = data.get("completed", False)
        task.created_at = datetime.fromisoformat(data["created_at"])
        
        return task
    
    def __str__(self):
        """字符串表示"""
        status = "✓" if self.completed else " "
        priority_symbols = {
            Priority.LOW: "▽",
            Priority.MEDIUM: "◇",
            Priority.HIGH: "▲"
        }
        
        return f"[{status}] {priority_symbols[self.priority]} {self.title}"
    
    def __repr__(self):
        """开发者表示"""
        return f"Task(title='{self.title}', completed={self.completed})"

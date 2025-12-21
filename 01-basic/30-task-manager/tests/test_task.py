# tests/test_task.py
import unittest
from datetime import datetime
from task_manager.task import Task, Priority, Category

class TestTask(unittest.TestCase):
    """测试Task类"""
    
    def test_task_creation(self):
        """测试任务创建"""
        task = Task("测试任务")
        
        self.assertEqual(task.title, "测试任务")
        self.assertFalse(task.completed)
        self.assertEqual(task.priority, Priority.MEDIUM)
    
    def test_empty_title_raises_error(self):
        """测试空标题抛出异常"""
        with self.assertRaises(ValueError):
            Task("")
    
    def test_mark_complete(self):
        """测试标记完成"""
        task = Task("测试")
        task.mark_complete()
        
        self.assertTrue(task.completed)
    
    def test_to_dict_and_from_dict(self):
        """测试序列化/反序列化"""
        task = Task("测试", priority=Priority.HIGH)
        
        data = task.to_dict()
        restored = Task.from_dict(data)
        
        self.assertEqual(restored.title, task.title)
        self.assertEqual(restored.priority, task.priority)

if __name__ == "__main__":
    unittest.main()

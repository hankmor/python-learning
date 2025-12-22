# renamer.py
import os
import re
import json
from datetime import datetime

class FileRenamer:
    """文件重命名器"""
    
    def __init__(self, directory):
        self.directory = directory
        self.changes = []  # 记录修改
    
    def add_prefix(self, files, prefix):
        """添加前缀"""
        for filepath in files:
            dirname = os.path.dirname(filepath)
            filename = os.path.basename(filepath)
            new_name = prefix + filename
            new_path = os.path.join(dirname, new_name)
            self.changes.append((filepath, new_path))
    
    def add_suffix(self, files, suffix):
        """添加后缀（在扩展名前）"""
        for filepath in files:
            dirname = os.path.dirname(filepath)
            filename = os.path.basename(filepath)
            name, ext = os.path.splitext(filename)
            new_name = name + suffix + ext
            new_path = os.path.join(dirname, new_name)
            self.changes.append((filepath, new_path))
    
    def replace_text(self, files, old_text, new_text):
        """替换文件名中的文本"""
        for filepath in files:
            dirname = os.path.dirname(filepath)
            filename = os.path.basename(filepath)
            new_name = filename.replace(old_text, new_text)
            new_path = os.path.join(dirname, new_name)
            if filepath != new_path:  # 只记录有变化的
                self.changes.append((filepath, new_path))
    
    def preview(self):
        """预览修改"""
        if not self.changes:
            print("没有要修改的文件")
            return
        
        print(f"\n将要进行 {len(self.changes)} 项修改：")
        print("-" * 60)
        for i, (old, new) in enumerate(self.changes, 1):
            old_name = os.path.basename(old)
            new_name = os.path.basename(new)
            print(f"{i}. {old_name} -> {new_name}")
        print("-" * 60)
    
    def execute(self):
        """执行重命名"""
        if not self.changes:
            print("没有要执行的操作")
            return
        
        success_count = 0
        for old_path, new_path in self.changes:
            try:
                os.rename(old_path, new_path)
                success_count += 1
            except Exception as e:
                print(f"错误：{old_path} -> {e}")
        
        print(f"\n成功重命名 {success_count}/{len(self.changes)} 个文件")
        
        # 保存操作历史
        self.save_history()
    
    def save_history(self):
        """保存操作历史（简化版）"""
        history_file = os.path.join(self.directory, "history.json")
        
        # 读取现有历史
        history = []
        if os.path.exists(history_file):
            try:
                with open(history_file, 'r', encoding='utf-8') as f:
                    history = json.load(f)
            except Exception:
                pass # Ignore errors reading history
        
        # 添加新记录
        history.append({
            'time': datetime.now().isoformat(),
            'changes': [(old, new) for old, new in self.changes]
        })
        
        # 保存
        try:
            with open(history_file, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: Could not save history: {e}")

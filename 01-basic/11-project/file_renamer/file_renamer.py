#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件批量重命名工具

用法：
    python file_renamer.py
"""

import os
import sys

# 添加当前目录到sys.path，确保能导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from renamer import FileRenamer
from utils import list_files

def main():
    print("=" * 60)
    print("文件批量重命名工具")
    print("=" * 60)
    
    # 获取目录
    directory = input("\n请输入目录路径（留空使用当前目录）：").strip()
    if not directory:
        directory = "."
    
    if not os.path.exists(directory):
        print(f"错误：目录 '{directory}' 不存在")
        return
    
    # 获取文件过滤条件
    extension = input("文件扩展名过滤（如.txt，留空跳过）：").strip()
    if not extension:
        extension = None
    
    # 列出文件
    files = list_files(directory, extension)
    
    if not files:
        print("没有找到符合条件的文件")
        return
    
    print(f"\n找到 {len(files)} 个文件")
    
    # 创建重命名器
    renamer = FileRenamer(directory)
    
    # 操作菜单
    while True:
        print("\n请选择操作：")
        print("1. 添加前缀")
        print("2. 添加后缀")
        print("3. 替换文本")
        print("4. 预览修改")
        print("5. 执行重命名")
        print("0. 退出")
        
        choice = input("\n请输入选择：").strip()
        
        if choice == "1":
            prefix = input("请输入前缀：")
            renamer.add_prefix(files, prefix)
            print("✓ 已添加前缀规则")
        
        elif choice == "2":
            suffix = input("请输入后缀：")
            renamer.add_suffix(files, suffix)
            print("✓ 已添加后缀规则")
        
        elif choice == "3":
            old_text = input("请输入要替换的文本：")
            new_text = input("请输入新文本：")
            renamer.replace_text(files, old_text, new_text)
            print("✓ 已添加替换规则")
        
        elif choice == "4":
            renamer.preview()
        
        elif choice == "5":
            renamer.preview()
            confirm = input("\n确认执行？(y/N)：").strip().lower()
            if confirm == 'y':
                renamer.execute()
                break
            else:
                print("已取消")
        
        elif choice == "0":
            print("再见！")
            break
        
        else:
            print("无效的选择")

if __name__ == "__main__":
    main()

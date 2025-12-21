"""
主程序入口
- 命令行交互界面
- 应用：函数、控制流程、异常处理
"""

from task_manager.task import Task, Priority, Category
from task_manager.manager import TaskManager
from task_manager.storage import TaskStorage
from datetime import datetime

def print_menu():
    """打印菜单"""
    print("\n" + "=" * 50)
    print("任务管理器")
    print("=" * 50)
    print("1. 查看所有任务")
    print("2. 添加任务")
    print("3. 完成任务")
    print("4. 删除任务")
    print("5. 搜索任务")
    print("6. 统计信息")
    print("0. 退出")
    print("=" * 50)

def display_tasks(tasks):
    """显示任务列表"""
    if not tasks:
        print("没有任务")
        return
    
    print("\n任务列表：")
    for i, task in enumerate(tasks):
        print(f"{i}. {task}")
        if task.due_date:
            print(f"   截止：{task.due_date.strftime('%Y-%m-%d')}")

def add_task_interactive(manager: TaskManager):
    """交互式添加任务"""
    print("\n添加新任务")
    
    title = input("标题：").strip()
    if not title:
        print("标题不能为空")
        return
    
    description = input("描述（可选）：").strip()
    
    print("优先级：1-低 2-中 3-高")
    priority_input = input("选择（默认2）：").strip() or "2"
    priority = Priority(int(priority_input))
    
    try:
        task = Task(
            title=title,
            description=description,
            priority=priority
        )
        manager.add_task(task)
        print("✓ 任务已添加")
    
    except ValueError as e:
        print(f"错误：{e}")

def main():
    """主函数"""
    print("欢迎使用任务管理器")
    
    # 初始化
    storage = TaskStorage()
    manager = TaskManager(storage)
    
    while True:
        print_menu()
        choice = input("\n请选择操作：").strip()
        
        try:
            if choice == "1":
                display_tasks(manager.get_all_tasks())
            
            elif choice == "2":
                add_task_interactive(manager)
            
            elif choice == "3":
                display_tasks(manager.get_all_tasks())
                index = int(input("请输入任务编号："))
                if manager.complete_task(index):
                    print("✓ 任务已完成")
                else:
                    print("无效的任务编号")
            
            elif choice == "4":
                display_tasks(manager.get_all_tasks())
                index = int(input("请输入任务编号："))
                if manager.delete_task(index):
                    print("✓ 任务已删除")
                else:
                    print("无效的任务编号")
            
            elif choice == "5":
                keyword = input("请输入搜索关键词：")
                results = manager.search_tasks(keyword)
                display_tasks(results)
            
            elif choice == "6":
                stats = manager.get_statistics()
                print(f"\n总任务数：{stats['total']}")
                print(f"已完成：{stats['completed']}")
                print(f"待完成：{stats['pending']}")
                print(f"  高优先级：{stats['high_priority']}")
                print(f"  中优先级：{stats['medium_priority']}")
                print(f"  低优先级：{stats['low_priority']}")
            
            elif choice == "0":
                print("再见！")
                break
            
            else:
                print("无效的选择")
        
        except Exception as e:
            print(f"发生错误：{e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()

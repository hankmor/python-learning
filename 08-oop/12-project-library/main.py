from library.book import PhysicalBook, EBook
from library.user import User
from library.system import Library

def main():
    # 创建图书馆
    library = Library("市图书馆")
    
    # 添加图书
    book1 = PhysicalBook("978-1", "Python编程", "作者A", "编程", "A-101")
    book2 = EBook("978-2", "数据结构", "作者B", "编程", 15.5)
    library.add_book(book1)
    library.add_book(book2)
    
    print("图书已添加")
    
    # 注册用户
    user = User("U001", "张三", "zhang@example.com")
    library.register_user(user)
    
    print("用户已注册")
    
    # 借阅流程
    print("\n--- 借阅 ---")
    print(library.borrow_book("U001", "978-1"))
    
    # 尝试借阅同一本
    try:
        library.borrow_book("U001", "978-1")
    except ValueError as e:
        print(f"借阅失败: {e}")
    
    print(library.borrow_book("U001", "978-2"))
    
    # 搜索
    print("\n--- 搜索 'Python' ---")
    results = library.search_books("Python")
    for book in results:
        print(book)
    
    # 统计
    print("\n--- 统计信息 ---")
    stats = library.get_statistics()
    print(f"总藏书：{stats['total_books']}")
    print(f"可借阅：{stats['available']}")
    print(f"已借出：{stats['borrowed']}")
    
    # 归还
    print("\n--- 归还 ---")
    print(library.return_book("U001", "978-1"))
    
    # 最终统计
    stats = library.get_statistics()
    print(f"归还后已借出：{stats['borrowed']}")

if __name__ == "__main__":
    main()

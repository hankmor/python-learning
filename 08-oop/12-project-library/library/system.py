from .book import Book, PhysicalBook, EBook
from .user import User
from .record import BorrowRecord

class Library:
    """图书馆类"""
    
    def __init__(self, name):
        self.name = name
        self.books = {}  # ISBN -> Book
        self.users = {}  # user_id -> User
        self.records = []  # BorrowRecord列表
    
    def add_book(self, book):
        """添加图书"""
        if book.isbn in self.books:
            raise ValueError(f"图书{book.isbn}已存在")
        self.books[book.isbn] = book
    
    def remove_book(self, isbn):
        """删除图书"""
        if isbn not in self.books:
            raise ValueError(f"图书{isbn}不存在")
        if self.books[isbn].is_borrowed:
            raise ValueError("图书已借出，无法删除")
        del self.books[isbn]
    
    def register_user(self, user):
        """注册用户"""
        if user.user_id in self.users:
            raise ValueError(f"用户{user.user_id}已存在")
        self.users[user.user_id] = user
    
    def borrow_book(self, user_id, isbn):
        """借阅图书"""
        # 验证
        if user_id not in self.users:
            raise ValueError("用户不存在")
        if isbn not in self.books:
            raise ValueError("图书不存在")
        
        user = self.users[user_id]
        book = self.books[isbn]
        
        if book.is_borrowed:
            raise ValueError("图书已被借出")
        if not user.can_borrow():
            raise ValueError("借阅数量已达上限")
        
        # 借阅
        book.is_borrowed = True
        user.borrow_book(isbn)
        record = BorrowRecord(user_id, isbn)
        self.records.append(record)
        
        return f"{user.name}成功借阅《{book.title}》"
    
    def return_book(self, user_id, isbn):
        """归还图书"""
        if user_id not in self.users:
            raise ValueError("用户不存在")
        if isbn not in self.books:
            raise ValueError("图书不存在")
        
        user = self.users[user_id]
        book = self.books[isbn]
        
        if not book.is_borrowed:
            raise ValueError("图书未被借出")
        
        # 归还
        book.is_borrowed = False
        user.return_book(isbn)
        
        # 更新记录
        for record in reversed(self.records):
            if (record.user_id == user_id and 
                record.isbn == isbn and 
                not record.return_date):
                record.mark_returned()
                break
        
        return f"{user.name}成功归还《{book.title}》"
    
    def search_books(self, keyword):
        """搜索图书"""
        results = []
        keyword = keyword.lower()
        for book in self.books.values():
            if (keyword in book.title.lower() or 
                keyword in book.author.lower() or
                keyword in book.category.lower()):
                results.append(book)
        return results
    
    def get_statistics(self):
        """获取统计信息"""
        total_books = len(self.books)
        borrowed = sum(1 for book in self.books.values() if book.is_borrowed)
        overdue = sum(1 for record in self.records if record.is_overdue)
        
        return {
            'total_books': total_books,
            'available': total_books - borrowed,
            'borrowed': borrowed,
            'total_users': len(self.users),
            'overdue_records': overdue
        }

class User:
    """用户类"""
    
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.borrowed_books = []  # ISBN列表
    
    def can_borrow(self, max_books=5):
        """检查是否可以借阅"""
        return len(self.borrowed_books) < max_books
    
    def borrow_book(self, isbn):
        """借阅图书"""
        if isbn not in self.borrowed_books:
            self.borrowed_books.append(isbn)
    
    def return_book(self, isbn):
        """归还图书"""
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'borrowed_books': self.borrowed_books
        }
    
    def __str__(self):
        return f"User({self.name}, 已借{len(self.borrowed_books)}本)"

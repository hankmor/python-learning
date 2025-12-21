from datetime import datetime, timedelta

class BorrowRecord:
    """借阅记录"""
    
    def __init__(self, user_id, isbn, borrow_date=None):
        self.user_id = user_id
        self.isbn = isbn
        self.borrow_date = borrow_date or datetime.now()
        self.return_date = None
        self.due_date = self.borrow_date + timedelta(days=30)
    
    @property
    def is_overdue(self):
        """是否逾期"""
        if self.return_date:
            return False
        return datetime.now() > self.due_date
    
    def mark_returned(self):
        """标记为已归还"""
        self.return_date = datetime.now()
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'isbn': self.isbn,
            'borrow_date': self.borrow_date.isoformat(),
            'due_date': self.due_date.isoformat(),
            'return_date': self.return_date.isoformat() if self.return_date else None
        }

from abc import ABC, abstractmethod

class Book(ABC):
    """图书抽象基类"""
    
    def __init__(self, isbn, title, author, category):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.category = category
        self.is_borrowed = False
    
    @abstractmethod
    def get_type(self):
        """获取图书类型"""
        pass
    
    def to_dict(self):
        """序列化"""
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'category': self.category,
            'is_borrowed': self.is_borrowed,
            'type': self.get_type()
        }
    
    def __str__(self):
        status = "已借出" if self.is_borrowed else "可借阅"
        return f"{self.title} by {self.author} ({status})"

class PhysicalBook(Book):
    """实体书"""
    def __init__(self, isbn, title, author, category, location):
        super().__init__(isbn, title, author, category)
        self.location = location  # 书架位置
    
    def get_type(self):
        return "physical"
    
    def to_dict(self):
        data = super().to_dict()
        data['location'] = self.location
        return data

class EBook(Book):
    """电子书"""
    def __init__(self, isbn, title, author, category, file_size):
        super().__init__(isbn, title, author, category)
        self.file_size = file_size  # 文件大小（MB）
    
    def get_type(self):
        return "ebook"
    
    def to_dict(self):
        data = super().to_dict()
        data['file_size'] = self.file_size
        return data

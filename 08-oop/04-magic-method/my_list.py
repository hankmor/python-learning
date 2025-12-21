class MyList:
    """自定义列表类"""
    def __init__(self, *items):
        self._items = list(items)
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
    
    def __delitem__(self, index):
        del self._items[index]
    
    def __iter__(self):
        return iter(self._items)
    
    def __contains__(self, item):
        return item in self._items
    
    def __add__(self, other):
        """支持+运算"""
        return MyList(*(self._items + other._items))
    
    def __mul__(self, n):
        """支持*运算"""
        return MyList(*(self._items * n))
    
    def __str__(self):
        return f"MyList({self._items})"
    
    def __repr__(self):
        return f"MyList{tuple(self._items)}"
    
    def append(self, item):
        """添加元素"""
        self._items.append(item)

if __name__ == "__main__":
    # 使用
    ml = MyList(1, 2, 3)
    print(len(ml))      # 3
    print(ml[0])        # 1
    print(2 in ml)      # True
    print(ml + MyList(4, 5))  # MyList([1, 2, 3, 4, 5])
    print(ml * 2)       # MyList([1, 2, 3, 1, 2, 3])

    for item in ml:
        print(item)

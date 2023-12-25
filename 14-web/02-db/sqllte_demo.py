"""
python 内置了对 sqlite 的支持，可以直接使用
"""

import sqlite3

# ================================================
# sqlite 基本操作
# ================================================

# # 连接到数据库，其实就是一个文件
# conn = sqlite3.connect('example.db')
# # 打开游标，就可以操作数据库了
# c = conn.cursor()
# # 创建表
# c.execute('''CREATE TABLE IF NOT EXISTS user(id integer PRIMARY KEY autoincrement, name varchar(32), age int)''')
# # 插入几条数据
# c.execute('''INSERT INTO user(name, age) VALUES ('hank', 20), ('jason', 18), ('jimmy', 15)''')
# # 插入后影响的行数
# print(c.rowcount)
# # 提交事务
# conn.commit()
# # 当然，也可以回滚事务
# # conn.rollback()
# # 最后，关闭连接
# conn.close()


# ================================================
# sqlite CRUD操作
# ================================================

DB = 'example.db'


def create_table():
    """创建表"""
    # 使用 with 语句就不用担心关闭连接的问题了
    with sqlite3.connect(DB) as conn:
        # 打开游标，就可以操作数据库了
        c = conn.cursor()
        # 删除已经存在的表
        c.execute('''DROP TABLE IF EXISTS user''')
        # 创建表
        c.execute('''CREATE TABLE user(id integer PRIMARY KEY autoincrement, name varchar(32), age int)''')
        # 提交事务
        conn.commit()


def insert_data():
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        # 插入几条数据
        data = [('hank', 20), ('jason', 18), ('jimmy', 15)]
        # sql 语句的参数，必须通过 tuple 传入，tuple 需要与之对应
        c.executemany('''INSERT INTO user(name, age) VALUES (?, ?)''', data)
        conn.commit()
        # 插入后影响的行数
        return c.rowcount


def delete_data(id):
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute('''DELETE FROM user WHERE id = ?''', (id,))
        conn.commit()
        return c.rowcount


def update_data(id, name, age):
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute('''UPDATE user SET name = ?, age = ? WHERE id = ?''', (name, age, id))
        conn.commit()
        return c.rowcount


def get_one(id):
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute('''SELECT * FROM user WHERE id = ?''', (id,))
        return c.fetchall()


def get_all():
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute('''SELECT * FROM user''')
        return c.fetchall()


create_table()
print(insert_data())
print(get_one(1))
print(update_data(1, 'hank1', 22))
print(get_one(1))
print(get_one(2))
print(get_one(3))
print(get_all())
print(delete_data(1))
print(get_all())

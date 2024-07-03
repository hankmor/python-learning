"""
python 操作 mysql
https://dev.mysql.com/doc/connector-python/en/

首先需要安装mysql驱动：pip install mysql-connector-python
"""

import functools
import mysql.connector


def connect(fn):
    @functools.wraps(fn)  # 包装后函数名称不变
    def wrapper(*args, **kw):
        # 连接数据库
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="123456",
            database="test",
        )
        if len(args) > 1:
            if isinstance(args[0], mysql.connector.CMySQLConnection):
                conn = args[0]
                args = args[1:]
        # 执行目标函数
        d = fn(conn, *args, **kw)
        # 关闭连接
        conn.close()
        return d

    return wrapper


@connect
def get_one(conn):
    c = conn.cursor()
    # 查询一条记录，注意MySQL中占位符是 %s, 参数必须是一个tuple
    c.execute("""SELECT * FROM user1 WHERE id = %s""", (1,))
    user = c.fetchone()  # 返回是一个 tuple
    return user


@connect
def desc_table(conn):
    """
    查询表结构，与数据库一致，返回的字段分别为：
    +------------+-----------------+------+-----+---------+----------------+
    | Field      | Type            | Null | Key | Default | Extra          |
    +------------+-----------------+------+-----+---------+----------------+
    | id         | bigint unsigned | NO   | PRI | NULL    | auto_increment |
    | created_at | datetime(3)     | YES  |     | NULL    |                |
    | updated_at | datetime(3)     | YES  |     | NULL    |                |
    | deleted_at | datetime(3)     | YES  | MUL | NULL    |                |
    | name       | varchar(32)     | YES  |     |         |                |
    | age        | bigint          | YES  |     | 0       |                |
    | dept       | varchar(20)     | YES  | UNI | NULL    |                |
    +------------+-----------------+------+-----+---------+----------------+\
    """
    c = conn.cursor()
    c.execute("DESC user1")
    tbl = c.fetchall()
    return tbl


@connect
def insert_many(conn):
    # 打开游标
    c = conn.cursor()
    # 插入多条记录
    users = [("hank", 20), ("jason", 18)]
    # mysql 没有自动转换的方式，只能手动拼接sql
    s = ",".join(["(" + ",".join(["%s"] * len(users)) + ")"] * len(users[0]))
    sql = """INSERT INTO user1 (name, age) VALUES %s""" % s
    print(sql)
    args = []
    for user in users:
        args.append(user[0])
        args.append(user[1])
    # 参数只能为 tuple
    c.execute(sql, tuple(args))
    # c.execute('''INSERT INTO user1 (name, age) VALUES (%s, %s),(%s, %s)''', ('hank', 20, 'jason', 18))
    # 还可以使用 dict 用作命名参数
    c.execute(
        """INSERT INTO user1 (name, age) VALUES (%(name)s, %(age)s)""",
        {"name": "zhangsan", "age": 20},
    )
    conn.commit()  # 别忘了提交事务
    return c.rowcount


@connect
def delete_by_name(conn, names):
    c = conn.cursor()
    # mysql 没有将 list 或者 tuple 转为参数的形式？需要手动拼sql
    # https://stackoverflow.com/questions/4574609/executing-select-where-in-using-mysqldb
    s = ",".join(["%s"] * len(names))
    c.execute("""DELETE FROM user1 WHERE name IN (%s)""" % s, names)
    conn.commit()
    return c.rowcount


@connect
def get_all(conn):
    c = conn.cursor()
    # 查询所有
    c.execute("""SELECT * FROM user1""")
    data = c.fetchall()  # 返回的是一个list
    return data


tbl = desc_table()
print(tbl)

print(delete_by_name(["hank", "jason"]))

r = insert_many()
print(r)

r = get_one()
print(r)
print(r[0])  # id
print(r[1])  # created_at

r = get_all()
print(len(r))
print(r[-1:])  # 这是一个 tuple
print("id: ", r[-1:][0][0])  # id
print("name: ", r[-1:][0][4])  # name
print("age: ", r[-1:][0][5])  # age

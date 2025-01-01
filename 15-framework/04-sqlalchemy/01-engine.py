from sqlalchemy import create_engine, text

# 创建 engine
# sqlite 表明使用 sqlite 数据库
# pysqlite 为于 sqlite 交互的标准库
# /:memory: 表明使用sqlite3中的内存数据库,便于测试
# echo 参数表明输出执行的sql语句
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# 获取连接
with engine.connect() as conn:
    # 执行sql, text() 方法用于构建文本sql
    result = conn.execute(text("select 'hello world'"))
    # 从输出可以看到, connect执行sql默认并不会自动提交事务
    print(result.all())

# commit as you go模式: 手动提交数据
with engine.connect() as conn:
    result = conn.execute(text("create table test (id int primary key, name text)"))
    conn.execute(
        text("insert into test (id, name) values (:id, :name)"),
        [{"id": 1, "name": "zhangsan"}, {"id": 2, "name": "lisi"}],
    )
    # 手动提交事务
    conn.commit()

# begin once 模式: 自动提交
with engine.begin() as conn:
    conn.execute(
        text("insert into test (id, name) values (:id, :name)"),
        [{"id": 3, "name": "wangwu"}],
    )

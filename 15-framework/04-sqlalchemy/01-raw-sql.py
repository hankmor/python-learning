from sqlalchemy import Integer, String, create_engine, text

# 创建 engine
# sqlite 表明使用 sqlite 数据库
# pysqlite 为于 sqlite 交互的标准库
# /:memory: 表明使用sqlite3中的内存数据库,便于测试
# echo 参数表明输出执行的sql语句
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


def connect_without_commit():
    # 获取连接
    with engine.connect() as conn:
        # 执行sql, text() 方法用于构建文本sql
        result = conn.execute(text("select 'hello world'"))
        # 从输出可以看到, connect执行sql默认并不会自动提交事务
        print(result.all())


def commit_manually():
    # commit as you go模式: 手动提交数据
    with engine.connect() as conn:
        result = conn.execute(text("create table test (id int primary key, name text)"))
        print("result: ", result)
        # 使用 executemany 插入多条记录, 参数为dict列表, 相当于为每一个dict执行一次insert,但是sqlalchemy会自动优化sql
        # executemany 不会返回结果集
        conn.execute(
            text("insert into test (id, name) values (:id, :name)"),
            [{"id": 1, "name": "zhangsan"}, {"id": 2, "name": "lisi"}],
        )
        # 手动提交事务
        conn.commit()


def begin_once_auto_commit():
    # begin once 模式: 自动提交
    with engine.begin() as conn:
        conn.execute(
            text("insert into test (id, name) values (:id, :name)"),
            [{"id": 3, "name": "wangwu"}],
        )


def query_result():
    with engine.connect() as conn:
        result = conn.execute(text("select * from test"))
        # print("result: ", result)  # CursorResult object
        # print("result: ", result.all())  # all rows
        # 不能重复读取,前边的print已经读取过了, 所以先注释print语句
        # 方式一: 按位置变量分配
        # for id, name in result:
        #     print(f"{id} - {name}")
        print("-----")
        # 方式二: 使用下标读取
        # for row in result:
        #     print(f"{row[0]} - {row[1]}")
        print("-----")
        # 方式三: 使用属性读取
        # for row in result:
        #     print(f"{row.id} - {row.name}")
        # 方式四: 使用mapping读取
        print("-----")
        for dict_row in result.mappings():
            print(f"{dict_row['id']} - {dict_row['name']}")
        print("-----")


def query_result_condition():
    with engine.connect() as conn:
        # 单一条件
        # result = conn.execute(text("select * from test where id = :id"), {"id": 3})
        # TODO: in 查询 not work
        ids = [3, 4]
        result = conn.execute(
            text("select * from test where id in :ids").bindparams(ids=ids)
            # .columns(id=Integer, name=String)
        )
        print("result: ", result.mappings().all())


connect_without_commit()
commit_manually()
begin_once_auto_commit()
query_result()
query_result_condition()

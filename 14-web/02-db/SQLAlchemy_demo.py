"""
ORM框架SQLAlchemy demo
安装：pip install sqlalchemy

https://docs.sqlalchemy.org/
"""
import sqlalchemy
import sqlalchemy.orm

# 创建对象基类
Base = sqlalchemy.orm.declarative_base()


# 创建 Model class
class User(Base):
    # 表的名称
    __tablename__ = 'user1'

    # 表结构
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(64))
    age = sqlalchemy.Column(sqlalchemy.Integer)
    dept = sqlalchemy.Column(sqlalchemy.String(32))
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime)
    deleted_at = sqlalchemy.Column(sqlalchemy.DateTime)


# 连接数据库, 格式：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# 创建DBSession
DBSession = sqlalchemy.orm.sessionmaker(bind=engine)

# 删除数据
session = DBSession()
# 先查询 name 为Bob的user
user = session.query(User).filter(User.name == 'Bob').one()
session.delete(user)
session.commit()
session.close()

# 插入数据

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 查询数据

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.name == 'hank').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('user:', user.name, user.age, user.dept)
# 使用pk获取一条记录
user = session.get_one(entity=User, ident=user.id)
print('user:', user.name, user.age, user.dept)
# 查询所有
users = session.query(User).all()
print('type:', type(user))
print("num:", len(users))
for user in users:
    print('user:', user.name, user.age, user.dept)
# select
stmt = sqlalchemy.select(User).where(User.name.in_(['hank', 'Bob']))
for user in session.scalars(stmt):
    print('user:', user.name, user.age, user.dept)
# 关闭Session:
session.close()

# 修改

session = DBSession()
# 查询揭露
stmt = sqlalchemy.select(User).where(User.name.__eq__('hank'))
user = session.scalar(stmt)
# 更新 age
user.age = 30
# 提交事务
session.commit()
# 再次查询结果
stmt = sqlalchemy.select(User).where(User.name.__eq__('hank'))
user = session.scalar(stmt)
print(user.age)
session.close()

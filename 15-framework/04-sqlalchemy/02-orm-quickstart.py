from typing import Optional, List
from sqlalchemy import String, create_engine, ForeignKey, select, update
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
    relationship,
)
from sqlalchemy.orm.path_registry import path_is_entity

# create engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


# delcare model
class Base(DeclarativeBase):
    pass


class User(Base):
    # define table name
    __tablename__ = "user"
    # 使用Mapped定义基本类型, 详细定义可以使用 mapped_column
    id: Mapped[int] = mapped_column(primary_key=True)
    # 字符串类型,长度通过 String 方法来指定
    name: Mapped[str] = mapped_column(String(30))
    # 如果该字段可以为 null, 则使用 Optional 方法来定义
    fullname: Mapped[Optional[str]]

    # 定义地址, 引用 Address 对象的 user 属性
    # relationship表明这个字段是一个关系映射字段,数据库并没有该字段
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    # print info
    def __repr__(self) -> str:
        return f"User(id={self.id!r},name={self.name!r},fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    # 定义引用关系, 指向User对象的addresses属性
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


# 创建表
def create_table():
    # 从Base继承的类会创建表
    Base.metadata.create_all(engine)
    """output:
    CREATE TABLE user (
        id INTEGER NOT NULL,
        name VARCHAR(30) NOT NULL,
        fullname VARCHAR,
        PRIMARY KEY (id)
    )
    CREATE TABLE address (
            id INTEGER NOT NULL,
            email_address VARCHAR NOT NULL,
            user_id INTEGER NOT NULL,
            PRIMARY KEY (id),
            FOREIGN KEY(user_id) REFERENCES user (id)
    )
    """


def add_all():
    with Session(engine) as session:
        # 创建几个user
        spongebob = User(
            name="spongebob",
            fullname="Spongebob Squarepants",
            addresses=[Address(email_address="spongebob@sqlalchemy.org")],
        )
        sandy = User(
            name="sandy",
            fullname="Sandy Cheeks",
            addresses=[
                Address(email_address="sandy@sqlalchemy.org"),
                Address(email_address="sandy@squirrelpower.org"),
            ],
        )
        patrick = User(name="patrick", fullname="Patrick Star")
        # 调用 add_all
        session.add_all([spongebob, sandy, patrick])
        session.commit()


def select_query():
    session = Session(engine)
    stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
    # SELECT user.id, user.name, user.fullname
    # FROM user
    # WHERE user.name IN (?, ?)
    for user in session.scalars(stmt):
        print(user)


def select_with_join():
    session = Session(engine)
    stmt = (
        select(Address)
        .join(Address.user)
        .where(User.name == "sandy")
        .where(Address.email_address == "sandy@sqlalchemy.org")
    )
    # SELECT address.id, address.email_address, address.user_id
    # FROM address JOIN user ON user.id = address.user_id
    # WHERE user.name = ? AND address.email_address = ?
    sandy_addresses = session.scalars(stmt).all()
    for address in sandy_addresses:
        print(address)


def update_one():
    session = Session(engine)
    # select one
    stmt = select(User).where(User.name == "patrick")
    patrick = session.scalars(stmt).one()
    # append an address to patrick
    patrick.addresses.append(Address(email_address="patrick@sqlalchemy.org"))
    # INSERT INTO address (email_address, user_id) VALUES (?, ?)
    # ('patrick@sqlalchemy.org', 3)
    session.commit()

    # query and update address
    patrick_address = session.scalars(
        select(Address).where(Address.user_id == patrick.id)
    ).one()
    patrick_address.email_address = "patrickstar@sqlalchemy.org"
    # UPDATE address SET email_address=? WHERE address.id = ?
    # ('patrickstar@sqlalchemy.org', 4)
    session.commit()


def delete_cascade():
    session = Session(engine)
    # SELECT user.id AS user_id, user.name AS user_name, user.fullname AS user_fullname
    # FROM user
    # WHERE user.id = ?
    sandy = session.get(User, 2)
    # sandy 有多个 addresses, 查出一个并删除它
    # SELECT address.id, address.email_address, address.user_id
    # FROM address
    # WHERE address.email_address = ?
    sandy_address = session.scalars(
        select(Address).where(Address.email_address == "sandy@sqlalchemy.org")
    ).one()
    # 延迟加载sandy的addresses集合, 并删除指定的对象
    # SELECT address.id AS address_id, address.email_address AS address_email_address, address.user_id AS address_user_id
    # FROM address
    # WHERE ? = address.user_id
    #
    # DELETE FROM address WHERE address.id = ?
    sandy.addresses.remove(sandy_address)
    # flush 会发出delete sql, 而无需提交事务
    session.flush()


def delete_obj():
    session = Session(engine)
    patrick = session.scalars(select(User).where(User.name == "patrick")).one()
    session.delete(patrick)
    session.commit()


create_table()
add_all()
select_query()
select_with_join()
update_one()
delete_cascade()

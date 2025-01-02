from typing import Optional, List
from sqlalchemy import String, create_engine, ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
    relationship,
)

# create engine
engine = create_engine("sqlite+pysqlite:///", echo=True)


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


# create_table()

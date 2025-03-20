from datetime import datetime

from sqlalchemy import (
    Float,
    ForeignKey,
    Integer,
    Identity,
    String,
    DateTime,
    Text,
    text
)
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func


from sqlalchemy_train.sql_queries import Base, engine


class Role(Base):
    __tablename__ = 'roles'

    id: Mapped[int] = mapped_column(
        Integer,
        Identity(always=True),
        primary_key=True,
        autoincrement=True,
    )
    name: Mapped[str] = mapped_column(String(10), nullable=False)

    users: Mapped[list['User']] = relationship(
        'User',
        back_populates='role',
        cascade="all, delete",
        passive_deletes=True,
    )


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        Integer,
        Identity(always=True),
        primary_key=True,
        autoincrement=True,
    )
    first_name: Mapped[str] = mapped_column(String(25))
    last_name: Mapped[str] = mapped_column(String(75))
    email: Mapped[str] = mapped_column(String(75), index=True)
    password: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id", ondelete="CASCADE"))
    rating: Mapped[float] = mapped_column(Float, server_default=text("'0'"))
    deleted: Mapped[int] = mapped_column(TINYINT(1), server_default=text("'0'"))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    role: Mapped['Role'] = relationship('Role', back_populates='users')
    news: Mapped[list['News']] = relationship(
        'News',
        uselist=True,
        back_populates='author',
        cascade="all, delete",
        passive_deletes=True,
    )
    comments: Mapped[list['Comment']] = relationship(
        'Comment',
        uselist=True,
        back_populates='author',
        cascade="all, delete",
        passive_deletes=True,
    )


class News(Base):
    __tablename__ = 'news'

    id: Mapped[int] = mapped_column(
        Integer,
        Identity(always=True),
        primary_key=True,
        autoincrement=True,
    )
    title: Mapped[str] = mapped_column(String(75))
    body: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE")
    )
    moderated: Mapped[int] = mapped_column(TINYINT(1), server_default=text("'0'"))
    deleted: Mapped[int] = mapped_column(TINYINT(1), server_default=text("'0'"))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    author: Mapped['User'] = relationship('User', back_populates='news')
    comments: Mapped[list['Comment']] = relationship(
        'Comment',
        uselist=True,
        back_populates='news',
        cascade="all, delete",
        passive_deletes=True,
    )


class Comment(Base):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(
        Integer,
        Identity(always=True),
        primary_key=True,
        autoincrement=True,
    )
    body: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('users.id', ondelete="CASCADE")
    )
    news_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('news.id', ondelete="CASCADE")
    )
    deleted: Mapped[int] = mapped_column(TINYINT(1), server_default=text("'0'"))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    author: Mapped['User'] = relationship('User', back_populates='comments')
    news: Mapped[list['News']] = relationship('News', back_populates='comments')


Base.metadata.create_all(bind=engine)

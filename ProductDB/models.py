from sqlalchemy import (
    Column,
    String,Float,Boolean,Integer,
    ForeignKey
)

from sqlalchemy.orm import (
    declarative_base,
    relationship,
)
from connection import sqla_engine

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    products = relationship('Product', back_populates='category')

class Product(Base):
   __tablename__ = 'product'
   id = Column(Integer, primary_key=True)
   name = Column(String(100), nullable=False)
   price = Column(Float, nullable=False)
   in_stock = Column(Boolean, default=False)

   category_id = Column(Integer, ForeignKey('categories.id'))
   category = relationship('Category', back_populates='products')

products = relationship('Product', back_populates='category')

Base.metadata.create_all(bind=sqla_engine)


import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Authors(Base):
    __tablename__ = 'authors'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement="auto")
    name = sq.Column(sq.String(length=255), unique=True, nullable=False)

class Publisher(Base):
    __tablename__ = "publisher"
    id = sq.Column(sq.Integer, primary_key=True, autoincrement="auto")
    name = sq.Column(sq.String(length=255), unique=True, nullable=False)   


class Book(Base):
    __tablename__ = "book"
    id = sq.Column(sq.Integer, primary_key=True, autoincrement="auto")
    title = sq.Column(sq.String(255), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey(Publisher.id), nullable=False)
    author_id = sq.Column(sq.Integer, sq.ForeignKey(Authors.id), nullable=False)
    publisher = relationship(Publisher, backref="books")
    authors = relationship(Authors, backref="books")
 

class Shop(Base):
    __tablename__ = "shop"    
    id = sq.Column(sq.Integer, primary_key=True, autoincrement="auto")
    name = sq.Column(sq.String(length=255), unique=True, nullable=False)


class Stock(Base):
    __tablename__ = "stock"
    id = sq.Column(sq.Integer, primary_key=True, autoincrement="auto")
    id_book = sq.Column(sq.Integer, sq.ForeignKey(Book.id), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey(Shop.id), nullable=False)
    shops = relationship(Shop, backref="stoks")
    books = relationship(Book, backref="stoks")

class Sale(Base):
    __tablename__ = "sale"
    id = sq.Column(sq.Integer, primary_key=True, autoincrement="auto")
    price = sq.Column(sq.BigInteger, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey(Stock.id), nullable=False)
    stoks = relationship(Stock, backref="sales")

def create_tables(engine):
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
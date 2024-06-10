import sqlalchemy
from sqlalchemy.orm import sessionmaker
from publisher_models import create_tables, Publisher, Book, Stock, Shop, Sale, Authors

DSN = 'postgresql://postgres:password@192.168.32.215:5432/publisherdb'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

#для проверки в базе Ленин, Рэнд, Пушкин

author_name = input('Введите имя автора:')

from sqlalchemy.orm import aliased
a = aliased(Authors)
b = aliased(Book)
p = aliased(Publisher)
s = aliased(Stock)
sl = aliased(Sale)
myquery = session.query(a, b, p, s, sl).join(b, a.id == b.author_id).join(p, b.id_publisher == p.id).join(s, b.id == s.id_book ).join(sl, s.id == sl.id_stock).filter(a.name.like('%'+ author_name + '%')).order_by(sl.date_sale).all()
for a,b,p,s,sl in myquery:
    print(a.name, b.title, p.name, sl.price, sl.date_sale)

session.close()

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from publisher_models import create_tables, Publisher, Book, Stock, Shop, Sale, Authors

DSN = 'postgresql://postgres:password@192.168.32.215:5432/publisherdb'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

#Записываем данные в таблицу authors (insert)
#author1 = Authors(name='Сталин.И.В')
#author2 = Authors(name='Путин В.В')
#session.add(author1)
#добавить несколько значений.
#session.add_all([author1, author2])
#session.commit()

#Читаем данные из таблицы. (select) фильтруем по id 1
author_name = input('Введите имя автора:')
#for author in session.query(Authors).filter(Authors.name.like('%' + author_id + '%')).all():
#for author in session.query(Authors).filter(Authors.id == author_id).all():
#    print(author.id, author.name)

from sqlalchemy.orm import aliased
a = aliased(Authors)
b = aliased(Book)
p = aliased(Publisher)
s = aliased(Stock)
sl = aliased(Sale)
#myquery = session.query(a, b).join(b, a.id == b.author_id).order_by(a.name).all()
myquery = session.query(a, b, p, s, sl).join(b, a.id == b.author_id).join(p, b.id_publisher == p.id).join(s, b.id == s.id_book ).join(sl, s.id == sl.id_stock).filter(a.name.like('%'+ author_name + '%')).order_by(sl.date_sale).all()
for a,b,p,s,sl in myquery:
    print(a.name, b.title, p.name, sl.price, sl.date_sale)

session.close()

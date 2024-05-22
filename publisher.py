import sqlalchemy
import os
from sqlalchemy.orm import sessionmaker
from publisher_models import create_tables, Publisher, Book, Stock, Shop, Sale
from sqlalchemy.orm import aliased

DSN = 'postgresql://postgres:password@192.168.32.215:5432/publisherdb'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

def get_shops (session, publisher_name):
    b = aliased(Book)
    p = aliased(Publisher)
    s = aliased(Stock)
    sl = aliased(Sale)

    myquery = session.query(b, p, s, sl).\
        join(p, b.id_publisher == p.id).\
        join(s, b.id == s.id_book ).\
        join(sl, s.id == sl.id_stock)\
        
    if publisher_name.isdigit():
        myquery = myquery.filter(p.id == publisher_name).\
        order_by(sl.date_sale).all() 
    else:    
        myquery = myquery.filter(p.name.like('%'+ publisher_name + '%')).\
        order_by(sl.date_sale).all()
    
    for b,p,s,sl in myquery:
        print(b.title, p.name, sl.price, sl.date_sale, sep=' | ',end='\n')    
    session.close()

if __name__ == "__main__":
    publisher_name = input('Введите название издательства:')
    get_shops(session, publisher_name)
import sqlalchemy
#from sqlalchemy.orm import sessionmaker

from sqlalchemy_models import create_tables

DSN = 'postgresql://postgres:password@192.168.32.215:5432/netology_db'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

#Session = sessionmaker(bind=engine)
session = Session()

session.close()

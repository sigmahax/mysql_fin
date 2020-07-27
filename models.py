from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists

DATABASE = f'mysql+pymysql://base:base@localhost/stocks'
if not database_exists(DATABASE):
    print('Creating database')
    create_database(DATABASE)
engine = create_engine(DATABASE, echo=True)

Base = declarative_base()


class Ticker(Base):
    __tablename__ = 'tickers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ticker = Column(String)

Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

t1 = Ticker(name='Nano Dimension', ticker='NNDM')

session.add(t1)
session.commit()

result = session.query(Ticker).all()
for row in result:
    print(row)

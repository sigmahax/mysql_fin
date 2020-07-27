from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

from sqlalchemy_utils import create_database, database_exists

DATABASE = f'mysql+pymysql://base:base@localhost/stocks'
if not database_exists(DATABASE):
    print('Creating database')
    create_database(DATABASE)

engine = create_engine(DATABASE, echo=True)

meta = MetaData()

tickers = Table(
    'tickers', meta,
    Column('id', Integer, primary_key = True),
    Column('name', String(64)),
    Column('ticker', String(16)),
)

meta.create_all(engine)


ins = tickers.insert().values(name='Apple', ticker='APPL')
print(ins)

print(ins.compile().params)
conn = engine.connect()
result = conn.execute(ins)


s = tickers.select().where(tickers.c.name=='Apple')
result = conn.execute(s)
for row in result:
    print(row)

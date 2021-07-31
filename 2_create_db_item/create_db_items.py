import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Candel, Ticker, Model
import random

engine = create_engine(os.environ.get('DATABASE_URL'))
Session = sessionmaker(bind=engine)
session = Session()

def insert_n_random_values_to_candels(n: int, tiker_name: str):
    ticker = session.query(Ticker).filter_by(name=tiker_name).one()

    for i in range(n):
        item = Candel()
        item.ticker_id = ticker.id
        item.value = random.randint(0, 9)

        session.add(item)
        
        if i % 10000 == 0:
            print(f'{i} rows inserted')
            session.commit()

def create_tiker(name: str):
    ticker = Ticker()
    ticker.name = name

    session.add(ticker)
    session.commit()

# create_tiker('AAPL')
# create_tiker('SBER')

insert_n_random_values_to_candels(1 * 1000 * 1000, 'AAPL')

session.close()